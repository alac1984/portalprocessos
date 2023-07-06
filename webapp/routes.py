from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel.ext.asyncio.session import AsyncSession

from api.routes import (
    retrieve_all_grupo,
    retrieve_grupo,
    retrieve_macroprocesso,
    create_grupo,
    create_macroprocesso,
)
from models.grupo import GrupoCreate
from models.macroprocesso import MacroprocessoCreate
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


@router.get("/grupo", response_class=HTMLResponse)
async def grupo_create(request: Request):
    return templates.TemplateResponse("create_grupo.html", {"request": request})


@router.post("/grupo", response_class=HTMLResponse)
async def grupo_create_post(
    request: Request,
    nome: str = Form(...),
    exibicao: str = Form(...),
    session: AsyncSession = Depends(get_session),
):
    grupo_create = GrupoCreate(nome=nome, nome_exibicao=exibicao)
    try:
        await create_grupo(grupo_create, session)
        toast = {"bg": "custom-toast-success", "message": "Grupo criado com sucesso"}
    except Exception:
        toast = {"bg": "custom-toast-error", "message": "Erro na criação do grupo"}

    context = {"request": request, "toast": toast}

    response = templates.TemplateResponse("create_grupo.html", context)

    return response


@router.get("/macroprocesso/{macroprocesso_id}", response_class=HTMLResponse)
async def macroprocesso_detail(
    request: Request,
    macroprocesso_id: int,
    session: AsyncSession = Depends(get_session),
):
    macro = await retrieve_macroprocesso(macroprocesso_id, session)
    return templates.TemplateResponse(
        "macroprocesso.html", {"request": request, "macro": macro}
    )


@router.get("/macroprocesso", response_class=HTMLResponse)
async def macroprocesso_create(
    request: Request, session: AsyncSession = Depends(get_session)
):
    grupos = await retrieve_all_grupo(session)
    return templates.TemplateResponse(
        "create_macro.html", {"request": request, "grupos": grupos}
    )


@router.post("/macroprocesso", response_class=HTMLResponse)
async def macroprocesso_create_post(
    request: Request,
    nome: str = Form(...),
    exibicao: str = Form(...),
    grupo: int = Form(...),
    session: AsyncSession = Depends(get_session),
):
    breakpoint()
    macro_create = MacroprocessoCreate(
        nome=nome, nome_exibicao=exibicao, grupo_id=grupo
    )
    try:
        await create_macroprocesso(macro_create, session)
        toast = {
            "bg": "custom-toast-success",
            "message": "Macroprocesso criado com sucesso",
        }
    except Exception:
        toast = {
            "bg": "custom-toast-error",
            "message": "Erro na criação do macroprocesso",
        }

    context = {"request": request, "toast": toast}

    response = templates.TemplateResponse("create_macro.html", context)

    return response
