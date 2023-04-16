### Unit Simplifier Program

- To run the program, execute the SimplyUnit.py file.

    E.g :
```python
import UnitSimplifier as Us

units = "Nm⁻²⁴kJs⁻¹km⁻²¹kJ⁻²m⁻²/km⁻²s⁻¹"
print(f"Simplified Result  : {Us.UnitSimplifying(units)}")
```
    output : 
        >>   Units for simplify : Nm⁻²⁴kJs⁻¹km⁻²¹kJ⁻²m⁻²/km⁻²s⁻¹
             Simplified Result  : Nm⁻²⁶kJ⁻¹km⁻¹⁹

e.g :

    units = "Nm⁻²⁴kJs⁻¹km⁻²¹kJ⁻²m⁻² - km⁻²s⁻¹s⁴ + km⁻²s⁻¹s³ + kJ⁻²s⁻²/km⁻²s⁻¹"
    
    output : 
        >>   Units for simplify : Nm⁻²⁴kJs⁻¹km⁻²¹kJ⁻²m⁻² - km⁻²s⁻¹s⁴ + km⁻²s⁻¹s³ + kJ⁻²s⁻²/km⁻²s⁻¹
             Simplified Result  : Nm⁻²⁶kJ⁻¹s⁻¹km⁻²¹ - km⁻²s³ + km⁻²s² + kJ⁻²s⁻¹km²
