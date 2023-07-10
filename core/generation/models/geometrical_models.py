from typing import Any

from pydantic import BaseModel, NonNegativeFloat


class Cartesian(BaseModel):
    x: float
    y: float | None
    z: float | None


class Fiber(BaseModel):
    center: Cartesian
    radius: NonNegativeFloat


class InterFiberDistace(BaseModel):
    first: NonNegativeFloat
    second: NonNegativeFloat | None
    third: NonNegativeFloat | None


class Void(BaseModel):
    volume: NonNegativeFloat
    volume_fraction: NonNegativeFloat


class Domain(BaseModel):
    lenght: float
    breath: float
    depth: float


class Packing(BaseModel):
    fibers: list[Fiber]
    voids: list[Void]


class SpherialVoid(BaseModel):
    size: Void
    position: Cartesian
    radius: float
