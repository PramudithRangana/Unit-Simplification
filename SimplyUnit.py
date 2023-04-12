import UnitSimplifier as Us

# units = "Nm⁻²⁴kJs⁻¹km⁻²¹kJ⁻²m⁻²/km⁻²s⁻¹"
units = "Nm⁻²⁴kJs⁻¹km⁻²¹kJ⁻²m⁻² + km⁻²s⁻¹s⁴"

print("Units for simplify :", units)

print(f"Simplified Result  : {Us.UnitSimplifying(units)}")
