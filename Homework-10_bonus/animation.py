from matplotlib import animation


def animate_three_body_problem(fig, ax, positions):

    raise NotImplementedError


def update_plot(time_step, bodies, orbits, positions):
    """ Updates the underlying data of bodies and orbits for one time step. """
    
    x1, y1, z1, x2, y2, z2, x3, y3, z3 = positions

    orbits[0].set_data(x1[:time_step], y1[:time_step])
    orbits[0].set_3d_properties(z1[:time_step])

    orbits[1].set_data(x2[:time_step], y2[:time_step])
    orbits[1].set_3d_properties(z2[:time_step])

    orbits[2].set_data(x3[:time_step], y3[:time_step])
    orbits[2].set_3d_properties(z3[:time_step])

    bodies[0].set_offsets([x1[time_step], y1[time_step]])
    bodies[0].set_3d_properties(z1[time_step], "z")

    bodies[1].set_offsets([x2[time_step], y2[time_step]])
    bodies[1].set_3d_properties(z2[time_step], "z")

    bodies[2].set_offsets([x3[time_step], y3[time_step]])
    bodies[2].set_3d_properties(z3[time_step], "z")
