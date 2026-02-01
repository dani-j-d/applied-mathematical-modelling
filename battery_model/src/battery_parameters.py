class BatteryParams:
    """
    Container for battery parameters and power schedules.
    """

    def __init__(self, capacity, eta, p_in, p_out):
        self.capacity = capacity
        self.eta = eta
        self.p_in = p_in
        self.p_out = p_out
