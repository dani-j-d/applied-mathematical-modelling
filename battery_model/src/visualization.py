import matplotlib.pyplot as plt
from pathlib import Path

def plot_soc(time, soc, save_path=None):
    plt.figure()
    plt.plot(time, soc)
    plt.xlabel("Time")
    plt.ylabel("State of Charge")
    plt.title("Battery Charge–Discharge Dynamics")
    plt.grid(True)

    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()
