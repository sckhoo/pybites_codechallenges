from typing import Dict, List

from fastapi import FastAPI, HTTPException
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


@app.post("/", status_code=201)
async def create_food(food: Food):
    """Endpoint from Bite 03"""
    foods[food.id] = food
    return food


@app.get("/", response_model=List[Food])
async def read_foods():
    """Endpoints from Bite 04"""
    return list(foods.values())


@app.get("/{food_id}", response_model=Food)
async def read_food(food_id: int):
    """Endpoints from Bite 04"""
    return foods[food_id]


# Create the update and delete endpoints here ...
@app.put("/{food_id}", status_code=200)
async def update_food(food_id : int, food: Food):
    # Update the key-value pair in the dictionary
    if food_id in foods:
        foods[food_id] = food
    else:
        raise HTTPException(status_code=404, detail="Food not found")

@app.delete("/{food_id}", status_code=200)
async def delete_food(food_id : int):
    # Update the key-value pair in the dictionary
    if food_id in foods:
        foods.pop(food_id)
        return (dict({'ok': True}))
    else:
        raise HTTPException(status_code=404, detail="Food not found")