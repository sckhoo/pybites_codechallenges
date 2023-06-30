from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, world!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": "Hello, {}".format(name)}

if __name__ == "__main__":
    app.run(debug=True)
