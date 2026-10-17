from fastapi import FastAPI
app = FastAPI()
@app.get("/shakal")
def main():
    return {"message": "Server is running"}