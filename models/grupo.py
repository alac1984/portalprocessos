from sqlmodel import SQLModel, Field


class GrupoBase(SQLModel):
    nome: str
    nome_exibicao: str


class Grupo(GrupoBase, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)


class GrupoCreate(GrupoBase):
    pass
