from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes import router as api_router
from webapp.routes import router as web_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router, prefix="/api")
app.include_router(web_router)
