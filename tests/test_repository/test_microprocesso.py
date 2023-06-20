import pytest

from models.microprocesso import Microprocesso, MicroprocessoCreate
from repository.microprocesso import (
    repo_create_microprocesso,
    repo_retrieve_microprocesso,
)


@pytest.mark.asyncio
async def test_repo_retrieve_microprocesso(test_session):
    microprocesso_id = 1

    micro = await repo_retrieve_microprocesso(microprocesso_id, test_session)

    assert isinstance(micro, Microprocesso)
    assert micro.id == 1


@pytest.mark.asyncio
async def test_repo_create_microprocesso(test_session):
    micro_create = MicroprocessoCreate(nome="micro", nome_exibicao="Micro", url="dummy")

    micro = await repo_create_microprocesso(micro_create, test_session)

    assert isinstance(micro, Microprocesso)


# @pytest.mark.asyncio
# async def test_repo_delete_macroprocesso(test_session):
#     macroprocesso_id = 2

#     macro = await repo_delete_macroprocesso(macroprocesso_id, test_session)

#     assert isinstance(macro, Macroprocesso)
