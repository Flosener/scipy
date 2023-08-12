from expyriment import design, control, stimuli, io, misc
import random

control.set_develop_mode(True)
design.defaults.experiment_background_colour = (255, 255, 255)
design.defaults.experiment_text_size = 40
stimuli.defaults.textline_text_size = 90
stimuli.defaults.fixcross_line_width = 2
stimuli.defaults.fixcross_size = (40,40)
io.defaults.outputfile_time_stamp = False

INSTRUCTION_TEXT = """In this task, you'll see a sequence of 1-6 numbers one after another. Then, after a short pause, you'll see another number (in red). Your task is to tell as quickly as possible if the red number was part of the sequence before or not. \n\n Try to answer as quick as possible using your keyboard: Press [Y] if the number was part of the sequence, and [N] if it wasn't. We'll start with a few practice trials before you can have a pause, before we start the real task. \n\n Press any key to start the practice."""
AFTER_PRACTICE_TEXT = "That was the practice. If you have any questions and there's an instructor nearby, ask your questions. If not, press any Key to continue to the first block."
PAUSE_TEXT = "This was the first block of the experiment. Make a pause and press any key to continue to the last block whenever you're ready."
GOODBYE_TEXT = "That's it! Thanks for participating in this study!"

def make_design(exp):

    raise NotImplementedError


def conduct_experiment(exp, response_keys, fixcross, blankscreen):
    for num, block in enumerate(exp.blocks):
        # show text according to block
        if num == 0:
            stimuli.TextScreen("Instructions", INSTRUCTION_TEXT, text_size=25).present()
            exp.clock.wait(1000)
        elif num == 1:
            stimuli.TextScreen("Pause", AFTER_PRACTICE_TEXT).present()
            exp.clock.wait(1000)
        elif num == 2:
            stimuli.TextScreen("Pause", PAUSE_TEXT).present()
            exp.clock.wait(1000)
        exp.keyboard.wait()
        for trial in block.trials:
            blankscreen.present()
            exp.clock.wait(1000 - trial.stimuli[0].preload())
            for num in range(len(trial.stimuli)-1):
                trial.stimuli[num].present()
                exp.clock.wait(1200 - trial.stimuli[num+1].preload() if num < len(trial.stimuli)-1 else 0)
            blankscreen.present()
            exp.clock.wait(1800)
            fixcross.present(clear=False, update=True)
            exp.clock.wait(100)
            blankscreen.present()
            exp.clock.wait(100 - trial.stimuli[-1].preload())
            # present the target number
            trial.stimuli[-1].present(clear=False)
            # wait for response
            key, rt = exp.keyboard.wait(keys=response_keys, duration=5000)
            user_thought = (key == response_keys[0])
            user_correct = (user_thought == trial.get_factor("does_appear"))
            # log trial condition, user response and reaction time
            exp.data.add([block.name, trial.get_factor("length"), trial.get_factor("does_appear"), user_correct, rt])


def main():
    # Create and initialize an Experiment
    exp = design.Experiment("Sternberg Task")
    control.initialize(exp)
    # esc key for quit
    exp.keyboard.set_quit_key(27)

    # Define and preload standard stimuli
    fixcross = stimuli.FixCross()
    fixcross.preload()
    blankscreen = stimuli.BlankScreen(colour=(255,255,255))
    blankscreen.preload()

    response_keys = [misc.constants.K_y, misc.constants.K_n]

    make_design(exp) #this is the function you're implementing!

    exp.data_variable_names = ["Block", "Length", "Does Appear", "Correct Answer", "Response Time"]
    exp.save_design('steinberg_task_design.csv')

    control.start()
    conduct_experiment(exp, response_keys, fixcross, blankscreen)
    control.end(goodbye_text= GOODBYE_TEXT)


if __name__ == "__main__":
    main()
