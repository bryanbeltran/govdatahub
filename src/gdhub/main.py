from fastapi import FastAPI

from gdhub.routers import health

app = FastAPI()
app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": "Hello, GovDataHub!"}
