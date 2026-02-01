# Modelling Principles and Assumptions

## General Modelling Philosophy
All models in this repository aim to balance simplicity and realism.
Models are constructed to capture dominant dynamics while remaining interpretable.

## Battery Model Assumptions
- Battery state is represented by a single variable: state of charge (SoC)
- Charging and discharging efficiencies are constant
- Temperature effects are neglected
- Battery degradation is neglected
- Power inputs are externally prescribed functions of time

The following assumptions underpin the battery model used in this project:

1. **Lumped System Model**  
   The battery is treated as a single energy reservoir with no spatial variations.

2. **Constant Efficiency**  
   Charging/discharging efficiency, η, is constant in time. Real batteries may vary with SoC, 
   temperature, and age, but this simplified assumption is standard for basic models.

3. **No Thermal/Degradation Effects**  
   The model does not include temperature dependence or capacity degradation.

4. **Input Power Profiles**  
   Inputs P_in and P_out are specified externally (from SQL) and assumed known ahead of time.

5. **State of Charge Bounds**  
   SoC is bounded between 0 and 1 (or 0% and 100%).
