import os
if 'HOME' not in os.environ:
    os.environ['HOME'] = os.path.abspath('.')
    
import pandas as pd
from expyriment import design, stimuli
from functools import reduce

def ignore_warnings_print(*args, **kwargs):
    if args[0] != "Warning: Stimulus created before initializing (experiment defaults won't apply)!":
        print(*args, **kwargs)

stimuli._visual.print = ignore_warnings_print #otherwise this warning would be printed 132 times

import sternberg_task
MODULE = sternberg_task
FILENAME = "sternberg_task_design.csv"

def get_first_row(filename):
    with open(filename, "r") as f:
        for num, line in enumerate(f.readlines()):
            if not line.strip().startswith("#"):
                return num

def test_sternberg_design():
    exp = design.Experiment("Sternberg Task")
    assert hasattr(MODULE, "make_design"), "You need to implement the function make_design!"
    MODULE.make_design(exp)
    exp.save_design(FILENAME)

    all_trials = []
    for num_block, block in enumerate(exp.blocks):
        assert type(block) == design._structure.Block, "You must provide Expyriment-Blocks!"
        for trial in block.trials:
            assert type(trial) == design._structure.Trial, "The Blocks must consist of Expyriment-Trials!"
            assert len(trial.stimuli) >= 2, "You need at least one digit and the target!"
            assert set(trial.factor_names) == set(["length", "does_appear"]), "Every Trial must have the factors 'length' and 'does_appear'!"
            assert all(type(i) == stimuli._textline.TextLine for i in trial.stimuli), "The respective stimuli must always be TextLines!"
            trial_nums = [int(i.text) for i in trial.stimuli[:-1]]
            all_trials.append({"num_block": num_block, "block": block.name,
                               "length": trial.get_factor("length"), "does_appear": trial.get_factor("does_appear"),
                               "numbers": trial_nums, "target": int(trial.stimuli[-1].text), "trial_id": trial.id})
    from_object = pd.DataFrame(all_trials)
    from_csv = pd.read_csv(FILENAME, skiprows=get_first_row(FILENAME))
    df = from_object.merge(from_csv, how="left", left_on=["trial_id", "num_block"], right_on=["trial_id", "block_cnt"])
    df = df.drop(["does_appear_y", "length_y", "block_cnt"], axis="columns").rename(columns={'does_appear_x': 'does_appear', 'length_x': 'length'})

    practice, block1, block2 = [ df[df["block_id"] == i] for i in range(3)]
    assert len(practice) == 12, "The Practice-Block must contain exactly 12 trials!"
    assert all(practice["block"] == "Practice"), "The Practice-Block must have the name 'Practice'!"
    assert len(block1) == len(block2) == 60, "The main-Blocks must contain exactly 60 trials!"
    assert all(block1["block"] == "First Block"), "The first block must be named 'First Block'!"
    assert all(block2["block"] == "Second Block"), "The second block must be named 'Second Block'!"

    equal_vals = []
    for block_num, block in enumerate([practice, block1, block2]):
        assert not all(block.iloc[i]["trial_id"] <= block.iloc[i+1]["trial_id"] for i in range(len(block)-1)), "You need to shuffle the stimuli inside the blocks!"
        for _, trial in block.iterrows():
            assert len(trial["numbers"]) == trial["length"], "You say you have X numbers, but have != X!"
            assert len(set(trial["numbers"])) == len(trial["numbers"]), "The numbers must be distinct numbers!"
            assert all(0<i<10 for i in trial["numbers"]), "It were supposed to be only numbers between 1 and 9!"
            if trial["does_appear"]:
                assert trial["target"] in trial["numbers"], "Where does_appear is true, the target must be one of the numbers!"
            else:
                assert not trial["target"] in trial["numbers"], "Where does_appear is false, the target must not be one of the numbers!"

        if block_num > 0: #these don't hold for the practice-block
            assert len(block[block["does_appear"]] == 30), "For the main blocks, there must be exactly thirty trials where the target does appear!"
            for num_numbers in range(1, 7):
                assert len(block[block["length"] == num_numbers] == 10), "For the main blocks, there must be exactly 10 trials with 1, 2, 3, 4, 5 and 6 numbers!"

            for num_numbers in range(1,7):
                for does_appear in [True, False]:
                    relevant_trials = block[(block["length"] == num_numbers) & (block["does_appear"] == does_appear)]
                    assert len(relevant_trials) == 5, "For the main blocks, there must be 5 conditions of each combination of [targetin, targetout], [num_numbers=1..6]!"

                    are_equal = []
                    for i in range(len(relevant_trials["numbers"])-1):
                        for j in range(i+1, len(relevant_trials["numbers"])):
                            are_equal.append(relevant_trials["numbers"].iloc[i] == relevant_trials["numbers"].iloc[j])
                    equal_vals.append(reduce(lambda x, y: x+y, are_equal))
    assert sum(equal_vals)/len(equal_vals) < 1, "Trials with the same conditions should still differ in general, don't simply copy trials!"
