class DCGenerator:
    def __init__(self, armature_resistance, field_resistance, load_resistance, emf):
        self.armature_resistance = armature_resistance
        self.field_resistance = field_resistance
        self.load_resistance = load_resistance
        self.emf = emf

    def calculate_current(self):
        total_resistance = self.armature_resistance + self.load_resistance
        current = self.emf / total_resistance
        return current

    def calculate_power(self):
        current = self.calculate_current()
        power = self.emf * current
        return power


class DCSeriesMotor:
    def __init__(self, armature_resistance, series_field_resistance, supply_voltage, back_emf):
        self.armature_resistance = armature_resistance
        self.series_field_resistance = series_field_resistance
        self.supply_voltage = supply_voltage
        self.back_emf = back_emf

    def calculate_current(self):
        total_resistance = self.armature_resistance + self.series_field_resistance
        current = (self.supply_voltage - self.back_emf) / total_resistance
        return current

    def calculate_torque(self, k_t):
        current = self.calculate_current()
        torque = k_t * current
        return torque


class DCShuntMotor:
    def __init__(self, armature_resistance, field_resistance, supply_voltage, back_emf):
        self.armature_resistance = armature_resistance
        self.field_resistance = field_resistance
        self.supply_voltage = supply_voltage
        self.back_emf = back_emf

    def calculate_armature_current(self):
        armature_current = (self.supply_voltage - self.back_emf) / self.armature_resistance
        return armature_current

    def calculate_field_current(self):
        field_current = self.supply_voltage / self.field_resistance
        return field_current

    def calculate_torque(self, k_t):
        armature_current = self.calculate_armature_current()
        torque = k_t * armature_current
        return torque


class DCCompoundMotor:
    def __init__(self, armature_resistance, series_field_resistance, shunt_field_resistance, supply_voltage, back_emf, type_compound):
        self.armature_resistance = armature_resistance
        self.series_field_resistance = series_field_resistance
        self.shunt_field_resistance = shunt_field_resistance
        self.supply_voltage = supply_voltage
        self.back_emf = back_emf
        self.type_compound = type_compound  # "long_shunt" or "short_shunt"

    def calculate_currents(self):
        if self.type_compound == "long_shunt":
            field_current = self.supply_voltage / self.shunt_field_resistance
            total_resistance = self.armature_resistance + self.series_field_resistance
            armature_current = (self.supply_voltage - self.back_emf) / total_resistance
        elif self.type_compound == "short_shunt":
            field_current = self.back_emf / self.shunt_field_resistance
            total_resistance = self.armature_resistance + self.series_field_resistance
            armature_current = (self.supply_voltage - self.back_emf) / total_resistance
        else:
            raise ValueError("Invalid compound type. Use 'long_shunt' or 'short_shunt'.")
        return armature_current, field_current

    def calculate_torque(self, k_t):
        armature_current, _ = self.calculate_currents()
        torque = k_t * armature_current
        return torque


# Example usage
if __name__ == "__main__":
    # DC Generator Example
    generator = DCGenerator(armature_resistance=0.5, field_resistance=100, load_resistance=10, emf=220)
    print("DC Generator Current:", generator.calculate_current())
    print("DC Generator Power:", generator.calculate_power())

    # DC Series Motor Example
    series_motor = DCSeriesMotor(armature_resistance=0.5, series_field_resistance=0.3, supply_voltage=220, back_emf=200)
    print("DC Series Motor Current:", series_motor.calculate_current())
    print("DC Series Motor Torque:", series_motor.calculate_torque(k_t=0.8))

    # DC Shunt Motor Example
    shunt_motor = DCShuntMotor(armature_resistance=0.5, field_resistance=100, supply_voltage=220, back_emf=200)
    print("DC Shunt Motor Armature Current:", shunt_motor.calculate_armature_current())
    print("DC Shunt Motor Field Current:", shunt_motor.calculate_field_current())
    print("DC Shunt Motor Torque:", shunt_motor.calculate_torque(k_t=0.8))

    # DC Compound Motor Example (Long Shunt)
    compound_motor_long = DCCompoundMotor(armature_resistance=0.5, series_field_resistance=0.3, shunt_field_resistance=100,
                                          supply_voltage=220, back_emf=200, type_compound="long_shunt")
    print("DC Compound Motor (Long Shunt) Currents:", compound_motor_long.calculate_currents())
    print("DC Compound Motor (Long Shunt) Torque:", compound_motor_long.calculate_torque(k_t=0.8))

    # DC Compound Motor Example (Short Shunt)
    compound_motor_short = DCCompoundMotor(armature_resistance=0.5, series_field_resistance=0.3, shunt_field_resistance=100,
                                           supply_voltage=220, back_emf=200, type_compound="short_shunt")
    print("DC Compound Motor (Short Shunt) Currents:", compound_motor_short.calculate_currents())
    print("DC Compound Motor (Short Shunt) Torque:", compound_motor_short.calculate_torque(k_t=0.8))
    