from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    i: int
    j: int


