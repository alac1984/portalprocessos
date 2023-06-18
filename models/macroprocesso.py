from sqlmodel import SQLModel, Field


class MacroprocessoBase(SQLModel):
    nome: str
    nome_exibicao: str
    grupo_id: int = Field(default=None, foreign_key="grupo.id")


class Macroprocesso(MacroprocessoBase, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)


class MacroprocessoCreate(MacroprocessoBase):
    ...
