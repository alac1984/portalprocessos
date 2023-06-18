"""macroprocesso_created

Revision ID: a436dbb69907
Revises: 4f28e5d2e9fa
Create Date: 2023-06-18 06:23:49.028777

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "a436dbb69907"
down_revision = "4f28e5d2e9fa"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "macroprocesso",
        sa.Column("nome", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("nome_exibicao", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("grupo_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["grupo_id"],
            ["grupo.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("macroprocesso")
    # ### end Alembic commands ###