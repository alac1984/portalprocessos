import pytest
from models.grupo import Grupo
from api.routes import retrieve_grupo
from api.routes import retrieve_macroprocesso
from api.routes import retrieve_all_grupo


@pytest.mark.asyncio
async def test_retrieve_grupo_success(test_session):
    grupo_id = 1

    grupo = await retrieve_grupo(grupo_id, test_session)

    assert grupo.id == 1


@pytest.mark.asyncio
async def test_retrieve_grupo_fail(test_session):
    grupo_id = 999

    grupo = await retrieve_grupo(grupo_id, test_session)

    assert grupo is None


@pytest.mark.asyncio
async def test_retrieve_all_grupo(test_session):
    grupos = await retrieve_all_grupo(test_session)

    assert isinstance(grupos, list)

    for grupo in grupos:
        assert isinstance(grupo, Grupo)


@pytest.mark.asyncio
async def test_retrieve_macroprocesso_success(test_session):
    macroprocesso_id = 1

    macroprocesso = await retrieve_macroprocesso(macroprocesso_id, test_session)

    assert macroprocesso.id == 1


@pytest.mark.asyncio
async def test_retrieve_macroprocesso_fail(test_session):
    macroprocesso_id = 999

    macroprocesso = await retrieve_macroprocesso(macroprocesso_id, test_session)

    assert macroprocesso is None
