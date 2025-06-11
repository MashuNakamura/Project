class Robot():
    def __init__(self, name: str, size: float, friend):
        self.name = name
        self.size = size
        self.friend: Robot | None = None