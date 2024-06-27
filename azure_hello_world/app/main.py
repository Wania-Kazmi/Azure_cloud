from typing import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    try:
        yield
    finally:
        yield

app = FastAPI(lifespan=lifespan, title="Azure Test Service API", version="0.0.1",
              servers=[
                  {
                      "url": "http://127.0.0.1:8000",
                      "description": "Development Server"
                  }
              ])


@app.get("/")
def read_root():
    return {"Hello": "Azure Test Service"}