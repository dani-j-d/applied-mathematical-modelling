def battery_ode(t, soc, params):
    """
    Battery charge–discharge dynamics.

    dS/dt = (eta * P_in(t) - P_out(t)) / C
    """
    return (params.eta * params.p_in(t) - params.p_out(t)) / params.capacity
