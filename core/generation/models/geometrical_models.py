from pydantic import BaseModel, NonNegativeFloat


class Fiber(BaseModel):
    center: list[float, float]
    radius: NonNegativeFloat


class InterFiberDistace(BaseModel):
    first: NonNegativeFloat
    second: NonNegativeFloat | None
    third: NonNegativeFloat | None


class Domain(BaseModel):
    x: float
    y: float
    z: float
