from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

# Path Parameters
@app.get("/items/{item_id}")
# async def read_items(item_id):
async def read_items(item_id: int):   #Path parameters with data types
    return {"item_id": item_id}

# Because path operations are evaluated in order, you need to make sure that the path for "/users/me" is declared before the one for "/users/{user_id}":
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
#Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me".
    

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
    # ModelName.model_name.value == "lenet"  # This is the same as above
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
# You could need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).
# In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.