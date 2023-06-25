from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    dashboard_content = templates.TemplateResponse(
        "dashboard.html", {"request": request}
    )
    return templates.TemplateResponse(
        "index.html", {"request": request, "default_content": dashboard_content}
    )


@router.get("/layouts", response_class=HTMLResponse)
async def layouts(request: Request):
    return templates.TemplateResponse("layouts.html", {"request": request})


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
