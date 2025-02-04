from dependency_injector import containers, providers
from src.infra.sensorapiclient.sensor_api_client import SensorApiClient
from src.infra.sqldb.db import get_db_session
from src.infra.sqldb.sql_device_repository import SQLDeviceRepository
from src.core.device.device_repository import DeviceRepository
from src.core.device.device_service import DeviceService
from src.core.device.device_summary_generator import DeviceSummaryGenerator
from src.core.sensor.sensor_data_repository import SensorDataRepository
from src.core.sensor.sensor_data_service import SensorDataService


class DIContainer(containers.DeclarativeContainer):
    db_session = providers.Resource(get_db_session)

    """
    sensor_data_repository: SensorDataRepository = providers.Factory(
        SQLSensorDataRepository,
        db_session=db_session
    )
    """
    sensor_data_repository: SensorDataRepository = providers.Singleton(
        SensorApiClient,
        base_url='http://localhost:5070'
    )

    sensor_data_service = providers.Factory(
        SensorDataService,
        sensor_data_repository=sensor_data_repository
    )

    device_repository: DeviceRepository = providers.Factory(
        SQLDeviceRepository,
        db_session=db_session
    )

    device_summary_generator = providers.Factory(
        DeviceSummaryGenerator,
        sensor_data_repository=sensor_data_repository
    )

    device_service = providers.Factory(
        DeviceService,
        device_repository=device_repository,
        device_summary_generator=device_summary_generator
    )

