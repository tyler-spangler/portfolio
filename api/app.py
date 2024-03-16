from fastapi import FastAPI, status

app = FastAPI()

@app.get("/health")
async def get_health():
    return {"health": status.HTTP_200_OK}