from datetime import datetime
from typing import Any

from passlib.context import CryptContext
from pydantic import BaseModel, computed_field

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# which we'll further explore in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0

food = Food(id=1, name='food', serving_size='bowl', kcal_per_serving=99, protein_grams=1.5, fibre_grams=1 )

# Write the User and FoodEntry models here ...

class User(BaseModel):
    id: int
    username: str
    password: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = get_password_hash(self.password)

user = User(id=1, username='sckhoo', password='password')

class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float
    
    @computed_field     #@property
    def total_calories(self) -> float:
        return self.number_servings * self.food.kcal_per_serving
    
foodentry = FoodEntry(id=1, user=user, food=food, date_added=datetime.now(), number_servings=2.5)

print(foodentry)

print(foodentry.total_calories)