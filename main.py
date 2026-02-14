from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from shapely.geometry import Polygon, MultiPolygon
import json
import os

app = FastAPI()

# Permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)




def calcular_bbox_esri(geometry):
    """
    Calcula bbox para geometría tipo ESRI (rings)
    """
    min_x = float("inf")
    min_y = float("inf")
    max_x = float("-inf")
    max_y = float("-inf")

    for ring in geometry["rings"]:
        for x, y in ring:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    return [min_x, min_y, max_x, max_y]


@app.get("/getjson")
def obtener_localidad(localidad: str = Query(...)):
    
    # Limpiar comillas si llegan
    localidad = localidad.replace('"', '').strip()

    archivo = f"{localidad}.json"
    print(archivo)
    if not os.path.exists(archivo):
        return {"error": "Localidad no encontrada"}

    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)

    geometry = data["geometry"]
    bbox = calcular_bbox_esri(geometry)

    return {
        "localidad": localidad,
        "bbox": bbox,
        "geojson": data,
        "arboles": None
    }
