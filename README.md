"""
Simulation API Documentation

Overview:
This FastAPI application simulates energy and CO2 values based on various user inputs. It allows users to filter simulations by PaaS, namespace, applications, and time range. Users can also select the hardware type and the percentage of change for the simulation. If the timeseries option is enabled, the API provides a graph of the simulated energy and CO2 values.

Setup:
- Prerequisites: Python 3.7+ and pip
- Installation: Clone the repository, navigate to the project directory, create and activate a virtual environment, and install the required packages.
- Running the Application: Start the application with the specified command. The application will be available at http://127.0.0.1:8000.

Usage:
- API Endpoints: The application has one endpoint, `/simulate`, which accepts a JSON object with the simulation parameters and returns the simulation results.
- Input Parameters: The available input parameters include `paas`, `namespace`, `applications`, `time_range`, `hardware_type`, `change_percentage`, and `timeseries`.
- Output: The API returns a JSON object with the simulated and computed energy and CO2 values, as well as the aggregated results. If `timeseries` is `true`, it also returns a PNG image of the graph showing the simulated and computed values over time.

Example Request: A sample request is provided in JSON format, demonstrating the structure and values of the input parameters.

Testing: The API endpoints can be tested using the Swagger UI at http://127.0.0.1:8000/docs.

Contributing: Contributions to the project are welcome. Please ensure to update tests as appropriate.

"""
# Simulation API Documentation

## Overview
This FastAPI application simulates energy and CO2 values based on various user inputs. It allows users to filter simulations by PaaS, namespace, applications, and time range. Users can also select the hardware type and the percentage of change for the simulation. If the timeseries option is enabled, the API provides a graph of the simulated energy and CO2 values.

## Setup

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory*.
3. Create a virtual environment:
>> python -m venv your-venv-name

4. Activate the virtual environment:
/**
 * Activates a virtual environment on Windows.
 * 
 * Usage:
 * - Windows: `your-venv-name\Scripts\activate`
 *   (If an error occurs, open a new PowerShell terminal and perform the following commands:
 *   - `Get-Executionpolicy`
 *   - `Set-Executionpolicy -Scope Process -Executionpolicy Bypass`
 *   - `.\your-venv-name\Scripts\Activate.ps1` )
 * - Linux or MacOS: `source venv/bin/activate`
 **/

5. Install the required packages:

`pip install -r requirements.txt`


### Running the Application
Start the application with the following command:

`uvicorn app.main:app --reload`

The application will be available at `http://127.0.0.1:8000`.

## Usage

### API Endpoints
- POST `/simulate`: This endpoint accepts a JSON object with the simulation parameters and returns the simulation results.

### Input Parameters
- `paas`: The Platform as a Service provider.
- `namespace`: The namespace for the simulation.
- `applications`: A list of applications to include in the simulation.
- `time_range`: A list containing the start and end times for the simulation.
- `hardware_type`: The type of hardware to simulate.
- `change_percentage`: The percentage change for the simulation.
- `timeseries`: A boolean value indicating whether a timeseries graph should be returned.

### Output
- If `timeseries` is `false`, the API returns a JSON object with the simulated and computed energy and CO2 values, as well as the aggregated results.
- If `timeseries` is `true`, the API returns a PNG image of the graph showing the simulated and computed values over time.

### Example Request
```json
POST /simulate
Content-Type: application/json

{
  "paas": "Azure",
  "namespace": "default",
  "applications": ["app1", "app2"],
  "time_range": ["2021-01-01T00:00:00Z", "2021-01-02T00:00:00Z"],
  "hardware_type": "TypeA",
  "change_percentage": 10.0,
  "timeseries": true
}

Response
The response will be a JSON object containing the simulation data or a PNG image of the graph, depending on the timeseries parameter.

Testing
You can test the API endpoints using the Swagger UI at http://127.0.0.1:8000/docs.

Contributing
Contributions to the project are welcome. Please ensure to update tests as appropriate.

License
Specify the license under which the project is made available.




































































































from fastapi import FastAPI
from .api.endpoints import router as api_router

app = FastAPI()

app.include_router(api_router)





-----------module---------

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




---------endpoints------------



from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from .models import SimulationInput, SimulationOutput
import matplotlib.pyplot as plt
from io import BytesIO

# Create a single instance of APIRouter which will be used for all the endpoints
router = APIRouter()

# Define the root endpoint which provides a JSON response when accessed
@router.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the Simulation API"})

# Define the '/simulate' endpoint which handles the simulation logic
@router.post("/simulate", response_model=SimulationOutput)
async def simulate(input: SimulationInput):
    # Placeholder for the actual simulation logic
    # You'll need to replace this with your computation code
    simulated_energy = [1, 2, 3]  # Example data
    computed_energy = [1.5, 2.5, 3.5]  # Example data
    simulated_co2 = [10, 20, 30]  # Example data
    computed_co2 = [15, 25, 35]  # Example data
    aggregated_co2 = sum(simulated_co2) + sum(computed_co2)
    aggregated_energy = sum(simulated_energy) + sum(computed_energy)

    if input.timeseries:
        # Generate and return the plot
        fig, ax = plt.subplots()
        ax.plot(simulated_energy, label='Simulated Energy', color='blue')
        ax.plot(computed_energy, label='Computed Energy', color='red')
        ax.set_xlabel('Time')
        ax.set_ylabel('Energy (kWh)')
        ax.legend()
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")
    else:
        # Return the data
        return SimulationOutput(
            simulated_energy=simulated_energy,
            computed_energy=computed_energy,
            simulated_co2=simulated_co2,
            computed_co2=computed_co2,
            aggregated_co2=aggregated_co2,
            aggregated_energy=aggregated_energy
        )









