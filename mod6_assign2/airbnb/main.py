from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Airbnb API is running"}
