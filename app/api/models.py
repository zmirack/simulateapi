from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class SimulationInput(BaseModel):
    paas: str
    namespace: str
    applications: List[str]
    time_range: List[datetime] = Field(..., min_items=2, max_items=2)
    hardware_type: str
    change_percentage: float
    timeseries: Optional[bool] = False

class SimulationOutput(BaseModel):
    simulated_energy: List[float]
    computed_energy: List[float]
    simulated_co2: List[float]
    computed_co2: List[float]
    aggregated_co2: float
    aggregated_energy: float