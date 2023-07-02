from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel.ext.asyncio.session import AsyncSession

from api.routes import retrieve_all_grupo, retrieve_grupo
from db.session import get_session

router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request, session: AsyncSession = Depends(get_session)):
    grupos = await retrieve_all_grupo(session)

    return templates.TemplateResponse(
        "index.html", {"request": request, "grupos": grupos}
    )


@router.get("/layouts", response_class=HTMLResponse)
async def layouts(request: Request):
    return templates.TemplateResponse("layouts.html", {"request": request})


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@router.get("/grupo/{grupo_id}", response_class=HTMLResponse)
async def grupo_detail(
    request: Request, grupo_id: int, session: AsyncSession = Depends(get_session)
):
    grupo = await retrieve_grupo(grupo_id, session)
    return templates.TemplateResponse(
        "grupo.html", {"request": request, "grupo": grupo}
    )
