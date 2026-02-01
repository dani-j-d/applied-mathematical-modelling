import numpy as np
from battery_model.src.battery_dynamics import battery_ode

def test_zero_power_gives_zero_derivative():
    class DummyParams:
        eta = 1.0
        capacity = 1.0
        p_in = lambda t: 0.0
        p_out = lambda t: 0.0

    dsdt = battery_ode(0.0, 0.5, DummyParams)
    assert np.isclose(dsdt, 0.0)

def test_soc_increases_when_input_greater_than_output():
    class Params:
        eta = 1.0
        capacity = 1.0
        p_in = lambda t: 1.0
        p_out = lambda t: 0.0
    
    derivative = battery_ode(0, 0.5, Params)
    assert derivative > 0
