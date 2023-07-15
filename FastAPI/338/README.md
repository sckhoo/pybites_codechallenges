Now with the Pydantic Food model defined we can start creating objects through FastAPI. Exciting!

In this Bite you will make a create_food() endpoint that receives a Food object payload and adds the food to a dictionary. We use an in memory data structure to keep things simple for starters. The endpoint should also return a status_code of 201 upon successful creation.

The foods dictionary will hold the food ids integers as keys and the Food objects as values.

After creation of a food object, foods will effectively hold the following (taken from the tests):

(Pdb) foods
{1: Food(id=1, name='egg', serving_size='piece', kcal_per_serving=78, protein_grams=6.3, fibre_grams=0)}
Note that we realize working with a global object is not ideal, but we wanted to separate FastAPI from SQLModel to teach this in a gradual manner.

Also this just teaches the happy path. In a later Bite we have you add some exception handling in case the object already exists or could not be created.

So go ahead and write this endpoint and look at the tests to see how we validate the code. Have fun!