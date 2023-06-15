from sqlmodel import SQLModel, Field


class MicroprocessoBase(SQLModel):
    nome: str
    nome_exibicao: str
    url: str


class Microprocesso(MicroprocessoBase, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    grupo_id: int = Field(default=None, foreign_key="macroprocesso.id")


class MicroprocessoCreate(MicroprocessoBase):
    ...
