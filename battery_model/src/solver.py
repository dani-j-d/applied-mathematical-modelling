from scipy.integrate import solve_ivp
from battery_model.src.battery_dynamics import battery_ode

def simulate_battery(params, S0, t_span, t_eval=None):
    """
    Simulate battery state of charge over time.
    """
    solution = solve_ivp(
        battery_ode,
        t_span,
        [S0],
        args=(params,),
        t_eval=t_eval,
        vectorized=False
    )
    return solution
