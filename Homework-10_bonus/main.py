from simulation import simulate_three_body_problem
from visualization import plot_three_body_problem
from animation import animate_three_body_problem

import matplotlib.pyplot as plt

INIT_STATE = (
    -0.50,  0.00,  0.00, # x1, y1, z1 = r1
     0.50,  0.00,  0.00, # x2, y2, z2 = r2
     0.00,  1.00,  0.00, # x3, y3, z3 = r3
     0.01,  0.01,  0.00, # vx1, vy1, vz1 = v1
    -0.05,  0.00, -0.19, # vx2, vy2, vz2 = v2
     0.00, -0.01,  0.00  # vx3, vy3, vz3 = v3
)

MASSES =  (1.10, 0.97, 1.00) # m1, m2, m3

N_TIME_STEPS = 500

PATH_OUT = "result/3bdy.gif"


def main():

    # simulate three-body problem
    print("Simulating three-body problem ...")
    positions = simulate_three_body_problem(INIT_STATE, MASSES, N_TIME_STEPS)

    # check simulation
    assert type(positions) == tuple, "Return a tuple of (x1, y1, z1, x2, y2, z2, x3, y3, z3) coordinates over time!"
    assert len(positions) == 9, "There should be 9 ndarrays of coordinates (3 for each of the 3 bodies)!"
    assert len(positions[0]) == N_TIME_STEPS, "There should be one value for each time step in x1!"
    assert positions[0][0] == INIT_STATE[0], "The first x1 coordinate should be the initial state x1 coordinate!"
    assert positions[4][0] == INIT_STATE[4], "The first y2 coordinate should be the initial state y2 coordinate!"
    assert positions[8][0] == INIT_STATE[8], "The first z3 coordinate should be the initial state z3 coordinate!"
        
    # plot three-body problem
    print("Plotting three-body problem ...")
    fig, ax = plot_three_body_problem(positions)
    plt.show()

    # check visualization
    assert len(ax.lines) == 3, "The calls to ax.plot should produce three lines objects!"
    assert len(ax.collections) == 3, "The calls to ax.scatter should produce three collection objects!"

    # animate three-body problem plot
    print("Animating three-body problem ...")
    anim = animate_three_body_problem(fig, ax, positions)

    # save three-body problem animation
    anim.save(PATH_OUT)
    print("Animation saved to '{}'.".format(PATH_OUT))


if __name__ == "__main__":
    main()
