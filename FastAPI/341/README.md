In order to measure daily food intake as a user our current Food model is not enough. We also need User and FoodEntry models, so let's create them!

In database-speak, FoodEntry is a many-to-many relation between User and Food. Users would add many foods and foods will be added by many users.

For this learning path, we'll work with these Pydantic models in memory to keep things simpler. In the SQLModel learning path we'll use a database.

Create the User and FoodEntry models based on what you learned in the second FastAPI Bite in this series.

Required attributes and their types:

User

- id -> int
- username -> str
- password -> str (needed for authentication later)

* For password override the constructor (__init__.py) to hash the password upon creation of the module. You can use the provided get_password_hash() function for this.

FoodEntry

- id -> int (what in a DB would be the primary key)
- user -> User (here we see that Pydantic models can be nested)
- food -> Food (from previous Bite and provided in the template)
- date_added -> datetime (defaults to datetime.now())
- number_servings -> float (fitness nerds can be quite exact about this)

* Additionally add a property to calculate the total calories of a food entry (number_servings * food.kcal_per_serving) and call it total_calories.

Good luck and in the next Bite we'll expand our API to work with these new objects.