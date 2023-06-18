import pytest
from api.routes import retrieve_grupo
from api.routes import retrieve_macroprocesso


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
async def test_retrieve_macroprocesso_success(test_session):
    macroprocesso_id = 1

    macroprocesso = await retrieve_macroprocesso(macroprocesso_id, test_session)

    assert macroprocesso.id == 1


@pytest.mark.asyncio
async def test_retrieve_macroprocesso_fail(test_session):
    macroprocesso_id = 999

    macroprocesso = await retrieve_macroprocesso(macroprocesso_id, test_session)

    assert macroprocesso is None
