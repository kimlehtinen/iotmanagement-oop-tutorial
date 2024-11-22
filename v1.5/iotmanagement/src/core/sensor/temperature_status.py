from enum import Enum


class TemperatureStatus(Enum):
    UNKNOWN = "UNKNOWN"
    NORMAL = "NORMAL"
    WARNING = "WARNING"
    DANGER = "DANGER"