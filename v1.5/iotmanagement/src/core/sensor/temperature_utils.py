from src.core.sensor.temperature_status import TemperatureStatus

class TemperatureUtils:
    def determine_status(self, temp_val: float) -> TemperatureStatus:
        if temp_val > 100:
            return TemperatureStatus.DANGER
        elif temp_val > 80:
            return TemperatureStatus.WARNING
        else:
            return TemperatureStatus.NORMAL
