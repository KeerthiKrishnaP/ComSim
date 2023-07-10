import numpy as np
from pydantic import BaseModel


class GaussainInput(BaseModel):
    standard_deviation: float
    mean: float


class GaussianDistribution(BaseModel):
    input: GaussainInput
    output: np.ndarray
