

class Device:
    id: str
    name: str
    location: str

    def __init__(
        self,
        id: str,
        name: str,
        location: str
    ):
        self.id = id
        self.name = name
        self.location = location
