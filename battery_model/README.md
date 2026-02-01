# Battery Charge–Discharge Dynamics

This model describes the temporal evolution of a battery's state of charge (SoC)
using a first-order differential equation.

The purpose of this model is to:
- Demonstrate mathematical modelling of an energy storage system
- Explore the relationship between charging power, discharging power, and capacity
- Provide a foundation for stochastic and optimization-based extensions

## Applications
- Renewable energy microgrids
- Energy storage systems
- Load balancing and peak shaving

## Modelling Approach
The system is modelled using ordinary differential equations (ODEs),
with parameters chosen to reflect physically realistic battery behaviour.

# Battery Charge–Discharge Model

This directory contains a modular Python implementation and a narrative Jupyter notebook 
for modelling battery state of charge (SoC) over time. It demonstrates:

1. A mathematical model of charging/discharging
2. SQL-driven input schedules
3. Numerical simulation using SciPy ODE solvers
4. Visualization of results

## Equation

We use an ODE to represent energy balance:

\[
\frac{dS}{dt} = \frac{\eta P_{\text{in}}(t) - P_{\text{out}}(t)}{C}
\]

## Inputs

Input power profiles are stored in SQLite and loaded via `db_utils.py`.

## Structure

- `src/` — reusable code
- `notebooks/` — Jupyter narrative
- `data/` — SQL database
- `figures/` — output plots
- `tests/` — minimal tests
