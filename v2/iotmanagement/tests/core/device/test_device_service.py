
from unittest.mock import MagicMock
import pytest

from src.core.device.device_repository import DeviceRepository
from src.core.device.device_service import DeviceService
from src.core.device.device import Device


@pytest.fixture
def device_repository() -> DeviceRepository:
    repo = MagicMock()
    def persist(item):
        return item

    repo.create.side_effect = persist
    repo.get_by_id.return_value = None

    return repo


@pytest.fixture
def device_summary_generator():
    return MagicMock()


@pytest.fixture
def sut(device_repository, device_summary_generator) -> DeviceService:
    return DeviceService(
        device_repository,
        device_summary_generator
    )


def test_create_device__cannot_create_device_when_id_exists(
    sut: DeviceService
):
    new_device = Device(
        id="RASPBERRY_PI_000001",
        name="New Raspberry Pi 1",
        location="Factory 1"
    )
    existing_device = Device(
        id="RASPBERRY_PI_000001",
        name="Existing Raspberry Pi 1",
        location="Factory 1"
    )

    sut.device_repository.get_by_id.return_value = existing_device

    with pytest.raises(ValueError) as ex:
        sut.create_device(new_device)

    assert str(ex.value) == "Device with id=RASPBERRY_PI_000001 already exists"


def test_create_device__can_create_device(
    sut: DeviceService
):
    new_device = Device(
        id="RASPBERRY_PI_000001",
        name="New Raspberry Pi 1",
        location="Factory 1"
    )

    result: Device = sut.create_device(new_device)

    assert result == new_device
    sut.device_repository.create.assert_called_once_with(new_device)

