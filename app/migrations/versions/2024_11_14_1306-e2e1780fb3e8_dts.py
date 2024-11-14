"""'dts'

Revision ID: e2e1780fb3e8
Revises: 
Create Date: 2024-11-14 13:06:44.033618

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e2e1780fb3e8"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "spycats",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("years_of_experience", sa.Integer(), nullable=False),
        sa.Column("breed", sa.String(length=100), nullable=False),
        sa.Column("salary", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_spycats")),
    )
    op.create_index(op.f("ix_spycats_id"), "spycats", ["id"], unique=False)
    op.create_index(op.f("ix_spycats_name"), "spycats", ["name"], unique=False)
    op.create_table(
        "missions",
        sa.Column("spy_cat_id", sa.Integer(), nullable=True),
        sa.Column("complete", sa.Boolean(), server_default="false", nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["spy_cat_id"], ["spycats.id"], name=op.f("fk_missions_spy_cat_id_spycats")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_missions")),
    )
    op.create_index(op.f("ix_missions_id"), "missions", ["id"], unique=False)
    op.create_table(
        "targets",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("country", sa.String(length=100), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("complete", sa.Boolean(), server_default="false", nullable=False),
        sa.Column("mission_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["mission_id"],
            ["missions.id"],
            name=op.f("fk_targets_mission_id_missions"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_targets")),
    )
    op.create_index(op.f("ix_targets_id"), "targets", ["id"], unique=False)
    op.create_index(op.f("ix_targets_name"), "targets", ["name"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_targets_name"), table_name="targets")
    op.drop_index(op.f("ix_targets_id"), table_name="targets")
    op.drop_table("targets")
    op.drop_index(op.f("ix_missions_id"), table_name="missions")
    op.drop_table("missions")
    op.drop_index(op.f("ix_spycats_name"), table_name="spycats")
    op.drop_index(op.f("ix_spycats_id"), table_name="spycats")
    op.drop_table("spycats")
    # ### end Alembic commands ###