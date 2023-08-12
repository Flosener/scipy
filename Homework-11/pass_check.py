from test_classification import test_find_closest_author
from test_synsets import test_get_noun_synsets
from test_pos import test_get_pos_freqs

import sys

SUBTASKS = {
    "POS Frequencies": (test_get_pos_freqs, 10),
    "Noun Synsets": (test_get_noun_synsets, 10),
    "Authorship Classification": (test_find_closest_author, 10)
}


def test_entire_homework():
    points_achieved = 0
    points_possible = 0

    print("Checking {} subtasks to see if you reached at least 2/3 of the possible points ...\n".format(len(SUBTASKS)))

    for subtask_name, (subtask_test_function, subtask_points) in SUBTASKS.items():

        points_possible += subtask_points

        try:

            subtask_test_function()

            # this line will only be reached if no AssertionError or other Exception was thrown in test_function()
            points_achieved += subtask_points

            print("Subtask '{}' with {} points: All good here!".format(subtask_name, subtask_points))

        except Exception as e:

            print("Subtask '{}' with {} points: Something went wrong. Exception: {}".format(subtask_name, subtask_points, e))

    if points_achieved >= (2 / 3) * points_possible:

        print("\nCongratulations! You passed this homework with {} out of {} points.".format(points_achieved,
                                                                                             points_possible))
        print("Do not forget to commit and push the current state of your code - the pass is only official once you see the checkmark on GitHub!")
        sys.exit(0)

    else:

        print("\nSorry! You only achieved {} points which is less than 2/3 of the possible {} points.".format(points_achieved, points_possible))
        sys.exit(1)


if __name__ == "__main__":
    test_entire_homework()
