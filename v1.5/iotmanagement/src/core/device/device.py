from uuid import UUID, uuid4


class Device:
    id: UUID
    name: str
    location: str

    def __init__(
        self,
        name: str,
        location: str,
        id: UUID = uuid4(),
    ):
        self.id = id
        self.name = name
        self.location = location
