from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class GeocodeRequest(BaseModel):
    address: str

class GeocodeResponse(BaseModel):
    latitude: float
    longitude: float

@app.post("/geocode", response_model=GeocodeResponse)
async def geocode(request: GeocodeRequest):
    # Use a free geocoding API — for example, OpenStreetMap's Nominatim
    url = os.getenv('URL_MAP')
    params = {
        "q": request.address,
        "format": "json",
        "limit": 1
    }
    
    headers = {
        "User-Agent": f"FastAPI-GeocodeApp/1.0 ({os.getenv('USER_EMAIL')})"
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            raise HTTPException(status_code=404, detail="Address not found")
        result = data[0]
        return GeocodeResponse(latitude=float(result["lat"]), longitude=float(result["lon"]))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Geocoding service error: {e}")
