from scipy import integrate, linalg

import numpy as np

K1 = 0.200
K2 = 7.239


def simulate_three_body_problem(init_state, masses, n_time_steps):

    raise NotImplementedError
    

def three_body_equations(t, state, m1, m2, m3):
    """ Simplified ODE system for three-body problem. """

    # unpack state
    r1, r2, r3, v1, v2, v3 = state.reshape(6, 3)

    # derivatives of velocities
    dv1_dt = -K1 * m2 * (r1-r2) / (linalg.norm(r1-r2)**3) - K1 * m3 * (r1-r3) / (linalg.norm(r1-r3)**3)
    dv2_dt = -K1 * m3 * (r2-r3) / (linalg.norm(r2-r3)**3) - K1 * m1 * (r2-r1) / (linalg.norm(r2-r1)**3)
    dv3_dt = -K1 * m1 * (r3-r1) / (linalg.norm(r3-r1)**3) - K1 * m2 * (r3-r2) / (linalg.norm(r3-r2)**3)

    # derivatives of positions
    dr1_dt = K2 * v1
    dr2_dt = K2 * v2
    dr3_dt = K2 * v3    

    # pack state
    derivatives = np.concatenate([dr1_dt, dr2_dt, dr3_dt, dv1_dt, dv2_dt, dv3_dt])

    return derivatives
