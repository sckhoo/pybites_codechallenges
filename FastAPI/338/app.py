from typing import Dict
import json
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


# write the Create endpoint
@app.post("/")
def create_food(infood : Dict):
    try:
        newfood = Food(**infood)
        foods[infood['id']] = newfood
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=infood)
    except:
        error = {
        "detail": [
            {
                "loc": ["body", "kcal_per_serving"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]}
        return JSONResponse(status_code=422, content=error)