from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    respond = {
        'message': "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"
    }
    return  respond
