from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcomeToKodeKloud():
    return {"message": "Welcome to KODEKLOUD!"}
