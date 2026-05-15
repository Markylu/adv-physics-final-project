class Body:
    pos: tuple[float, float]
    vel: tuple[float, float]
    mass: float
    radius: float

    def __init__(
        self,
        pos: tuple[float, float],
        vel: tuple[float, float],
        mass: float,
        radius: float,
    ) -> None:
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.radius = radius
