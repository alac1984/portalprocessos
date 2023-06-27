# mypy: disable-error-code=name-defined
from sqlmodel import SQLModel, Field, Relationship


class GrupoBase(SQLModel):
    nome: str
    nome_exibicao: str


class Grupo(GrupoBase, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    macroprocessos: list["Macroprocesso"] = Relationship(back_populates="grupo")  # noqa


class GrupoCreate(GrupoBase):
    pass
