# mypy: disable-error-code="name-defined"
from sqlmodel import SQLModel, Field, Relationship


class MacroprocessoBase(SQLModel):
    nome: str
    nome_exibicao: str
    grupo_id: int = Field(default=None, foreign_key="grupo.id")


class Macroprocesso(MacroprocessoBase, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    grupo: list["Grupo"] = Relationship(back_populates="macroprocessos")  # noqa
    microprocessos: list["Microprocesso"] = Relationship(  # noqa
        back_populates="macroprocesso"
    )


class MacroprocessoCreate(MacroprocessoBase):
    ...
