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
   `python -m venv your-venv-name`

4. Activate the virtual environment:

 > Activates a virtual environment on Windows:
 * Windows: `your-venv-name\Scripts\activate`
####  If an error occurs, open a new PowerShell terminal and perform the following commands:
    - `Get-Executionpolicy`
    - `Set-Executionpolicy -Scope Process -Executionpolicy Bypass`
    - `.\your-venv-name\Scripts\Activate.ps1` 
 > Activates a virtual environment on Linux/Mac:
 * Linux or MacOS: `source your-venv-name/bin/activate`
 

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

## Response
The response will be a JSON object containing the simulation data or a PNG image of the graph, depending on the timeseries parameter.

## Testing
You can test the API endpoints using the Swagger UI at http://127.0.0.1:8000/docs.


### Example Request

## json

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











