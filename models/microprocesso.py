# mypy: disable-error-code="name-defined"
from sqlmodel import SQLModel, Field, Relationship


class MicroprocessoBase(SQLModel):
    nome: str
    nome_exibicao: str
    macroprocesso_id: int = Field(default=None, foreign_key="macroprocesso.id")


class Microprocesso(MicroprocessoBase, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    macroprocesso: list["Macroprocesso"] = Relationship(  # noqa
        back_populates="microprocessos"
    )


class MicroprocessoCreate(MicroprocessoBase):
    ...
