Now that we're able to create and retrieve Food objects, it's time to add code to update and delete them.

Create the two corresponding endpoints:

1. To update, the API should

   1. receive a PUT request with the Food object's id and new / updated object

   2. update the item in the foods dictionary (to keep it simple, no need to update individual attributes, just swap out the whole Food object matching its id)

   3. return the updated item.

2. To delete the API should

   1. receive a DELETE request with the id of the food to be deleted

   2. delete it from the foods dictionary

   3. return a respone of {"ok": True} (as found here).

* We use PUT because we're replacing the whole item. For a partial update, PATCH would be the more appropriate HTTP verb / action.

For both endpoints raise an HTTPException with a status_code of 404 and message (detail) of Food not found, when the id passed in is not in the foods dictionary.

WIN: You have a simple API for food objects up and running with minimal code! We still need to add authentication, but first we'll make two more Pydantic models so that a user can start logging daily food intake.