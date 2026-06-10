from fastapi import FastAPI
from contextlib import asynccontextmanager

from rich import print, panel


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    print(panel.Panel("server started....", border_style="green"))
    yield
    print(panel.Panel("...stopped", border_style="red"))


app = FastAPI(lifespan=lifespan_handler)


@app.get("/")
def read_root():
    return {"detail": "server is running..."}
