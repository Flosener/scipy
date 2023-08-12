from test_mandelbrot import test_visualize_mandelbrot
from test_airquality import test_plot_airquality
from test_heatmap import test_make_heatmap

import sys

SUBTASKS = {
    "Plotting Air Quality": (test_plot_airquality, 10),
    "Making a Custom Heatmap": (test_make_heatmap, 10),
    "Visualizing Mandelbrot": (test_visualize_mandelbrot, 10)
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
        sys.exit(0)

    else:

        print("\nSorry! You only achieved {} points which is less than 2/3 of the possible {} points.".format(points_achieved, points_possible))
        sys.exit(1)

if __name__ == "__main__":
    test_entire_homework()
