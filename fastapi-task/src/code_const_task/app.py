from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .settings import settings
from .api import router


app = FastAPI()
app.include_router(router)
