# endpoints.py

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
from .models import SimulationInput, SimulationOutput
import matplotlib.pyplot as plt
from io import BytesIO
import os

# Create a single instance of APIRouter which will be used for all the endpoints
router = APIRouter()

# Define the root endpoint which provides a JSON response when accessed
@router.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the Simulation API"})

# Define the '/simulate' endpoint which handles the simulation logic
@router.post("/simulate", response_model=SimulationOutput)
async def simulate(input: SimulationInput):
    # Here you would implement your actual simulation logic
    # For now, we'll use some placeholder values that you should replace
    simulated_energy = [1 * input.change_percentage, 2 * input.change_percentage, 3 * input.change_percentage]
    computed_energy = [1.5 * input.change_percentage, 2.5 * input.change_percentage, 3.5 * input.change_percentage]
    simulated_co2 = [10 * input.change_percentage, 20 * input.change_percentage, 30 * input.change_percentage]
    computed_co2 = [15 * input.change_percentage, 25 * input.change_percentage, 35 * input.change_percentage]
    aggregated_co2 = sum(simulated_co2) + sum(computed_co2)
    aggregated_energy = sum(simulated_energy) + sum(computed_energy)

    # Save the plot to a file
    fig, ax = plt.subplots()
    ax.plot(simulated_energy, label='Simulated Energy', color='blue')
    ax.plot(computed_energy, label='Computed Energy', color='red')
    ax.set_xlabel('Time')
    ax.set_ylabel('Energy (kWh)')
    ax.legend()
    image_path = f'./graphs/{input.hardware_type}_graph.png'
    plt.savefig(image_path)
    plt.close(fig)

    if input.timeseries:
        # Return the plot as a streaming response
        return FileResponse(image_path, media_type="image/png")
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

# Define a GET endpoint to retrieve saved graph images
@router.get("/graphs/{hardware_type}")
async def get_graph(hardware_type: str):
    image_path = f'./graphs/{hardware_type}_graph.png'
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    else:
        raise HTTPException(status_code=404, detail="Graph not found")

