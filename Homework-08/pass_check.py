from test_load_data import test_load_data
from test_to_categorical import test_to_categorical
from test_seven_day_window import test_seven_day_window
import pytest
from sys import exit

SUBTASKS = {
    "Loading Data": (test_load_data, 10),
    "Creating Categorical Data": (test_to_categorical, 10),
    "Looking at weekly time windows": (test_seven_day_window, 10)
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

        except Exception:

            print("Subtask '{}' with {} points: Something went wrong. Better run 'pytest' on the corresponding pytest file to learn more!".format(subtask_name, subtask_points))
        
    if points_achieved >= (2/3) * points_possible:

        print("\nCongratulations! You passed this homework with {} out of {} points.".format(points_achieved, points_possible))
        print("Do not forget to commit and push the current state of your code - the pass is only official once you see the checkmark on GitHub!")
        exit(0)

    else:

        print("\nSorry! You only achieved {} points which is less than 2/3 of the possible {} points.".format(points_achieved, points_possible))
        exit(1)


if __name__ == "__main__":
    test_entire_homework()
