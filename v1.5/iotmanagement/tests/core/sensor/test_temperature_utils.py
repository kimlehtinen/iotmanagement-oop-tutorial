
import pytest

from src.core.sensor.temperature_utils import TemperatureUtils
from src.core.sensor.temperature_status import TemperatureStatus


@pytest.fixture
def sut() -> TemperatureUtils:
    return TemperatureUtils()


@pytest.mark.parametrize(
    "temp_val, expected_status",
    [
        (101, TemperatureStatus.DANGER),
        (100, TemperatureStatus.DANGER),
        (99, TemperatureStatus.WARNING),
        (80, TemperatureStatus.WARNING),
        (79, TemperatureStatus.NORMAL),
        (0, TemperatureStatus.NORMAL)
    ],
)
def test_determine_status(
    sut: TemperatureUtils,
    temp_val: float,
    expected_status: TemperatureStatus
):
    assert sut.determine_status(temp_val) == expected_status


@pytest.mark.parametrize(
    "temp_val",
    [
        "a",
        None,
        [],
        {},
        ()
    ],
)
def test_determine_status__raises_error_when_temp_val_is_not_a_number(
    sut: TemperatureUtils,
    temp_val
):
    with pytest.raises(TypeError):
        sut.determine_status(temp_val)
