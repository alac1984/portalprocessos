import pytest

from models.macroprocesso import Macroprocesso, MacroprocessoCreate
from repository.macroprocesso import (
    repo_create_macroprocesso,
    repo_retrieve_macroprocesso,
    repo_retrieve_all_macroprocesso,
    repo_delete_macroprocesso,
)


@pytest.mark.asyncio
async def test_repo_retrieve_macroprocesso(test_session):
    macroprocesso_id = 1

    macro = await repo_retrieve_macroprocesso(macroprocesso_id, test_session)

    assert isinstance(macro, Macroprocesso)
    assert macro.id == 1


@pytest.mark.asyncio
async def test_repo_retrieve_all_macroprocesso(test_session):
    macros = await repo_retrieve_all_macroprocesso(test_session)

    assert isinstance(macros, list)

    for macro in macros:
        assert isinstance(macro, Macroprocesso)


@pytest.mark.asyncio
async def test_repo_create_macroprocesso(test_session):
    macro_create = MacroprocessoCreate(nome="macro", nome_exibicao="Macro")

    macro = await repo_create_macroprocesso(macro_create, test_session)

    assert isinstance(macro, Macroprocesso)


@pytest.mark.asyncio
async def test_repo_delete_macroprocesso(test_session):
    macroprocesso_id = 2

    macro = await repo_delete_macroprocesso(macroprocesso_id, test_session)

    assert isinstance(macro, Macroprocesso)
