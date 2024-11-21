from dependency_injector import containers, providers

from iotmanagement.src.infra.sqldb.db import get_db_session

class DIContainer(containers.DeclarativeContainer):
    db_session = providers.Resource(get_db_session)
