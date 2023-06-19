import pytest

from models.grupo import Grupo, GrupoCreate
from repository.grupo import (
    repo_retrieve_grupo,
    repo_create_grupo,
    repo_retrieve_all_grupo,
)


@pytest.mark.asyncio
async def test_repo_retrieve_grupo(test_session):
    grupo_id = 1

    grupo = await repo_retrieve_grupo(grupo_id, test_session)

    assert isinstance(grupo, Grupo)
    assert grupo.id == 1


@pytest.mark.asyncio
async def test_repo_retrieve_all_grupo(test_session):
    grupos = await repo_retrieve_all_grupo(test_session)

    assert isinstance(grupos, list)

    for grupo in grupos:
        assert isinstance(grupo, Grupo)


@pytest.mark.asyncio
async def test_repo_create_grupo(test_session):
    grupo_create = GrupoCreate(nome="grupo", nome_exibicao="Grupo")

    grupo = await repo_create_grupo(grupo_create, test_session)

    assert isinstance(grupo, Grupo)
