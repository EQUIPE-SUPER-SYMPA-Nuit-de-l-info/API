from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoints.experience import experience_router


app = FastAPI()
app.include_router(experience_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
