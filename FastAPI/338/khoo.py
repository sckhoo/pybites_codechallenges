from typing import Dict
from pydantic import BaseModel

class Food(BaseModel):
    """Model from Bite 02"""
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0

def food_payload():
    return dict(
        id=1,
        name="egg",
        serving_size="piece",
        kcal_per_serving=78,
        protein_grams=6.3,
        fibre_grams=1,
    )

infood = food_payload()

print(infood)
newfood = Food
print(type(newfood))
for key in infood:
    newfood.key = infood[key]

for key in infood:
    print(newfood.key)
