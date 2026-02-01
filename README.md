# Applied Mathematical Modelling

This repository contains mathematical models of scientific and engineering systems.
Each model follows a structured approach:

1. Problem definition
2. Modelling assumptions
3. Mathematical formulation
4. Analytical and numerical analysis
5. Interpretation of results

## Models
- Battery charge–discharge dynamics (ODE-based model)

## Tools
Python, NumPy, SciPy, Matplotlib, Jupyter

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
