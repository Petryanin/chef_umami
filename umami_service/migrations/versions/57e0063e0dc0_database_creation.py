"""Database creation.

Revision ID: 57e0063e0dc0
Revises:
Create Date: 2023-09-17 00:57:18.091899
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "57e0063e0dc0"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade the database to a later version."""
    op.create_table(
        "ingredient",
        sa.Column("ingredient_id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=255), nullable=False),
        sa.PrimaryKeyConstraint("ingredient_id", name=op.f("ingredient_pkey")),
    )
    op.create_table(
        "recipe",
        sa.Column("recipe_id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=50), nullable=False),
        sa.Column("description", sa.VARCHAR(length=255), nullable=True),
        sa.Column("instructions", sa.TEXT(), nullable=True),
        sa.Column("cooking_time", sa.SMALLINT(), nullable=True),
        sa.Column("servings", sa.SMALLINT(), nullable=True),
        sa.Column("difficulty", sa.SMALLINT(), nullable=True),
        sa.Column("category", sa.SMALLINT(), nullable=True),
        sa.PrimaryKeyConstraint("recipe_id", name=op.f("recipe_pkey")),
    )
    op.create_table(
        "unit",
        sa.Column("unit_id", sa.INTEGER(), nullable=False),
        sa.Column("short_name", sa.VARCHAR(length=50), nullable=False),
        sa.Column("full_name", sa.VARCHAR(length=255), nullable=False),
        sa.PrimaryKeyConstraint("unit_id", name=op.f("unit_pkey")),
    )
    op.create_table(
        "recipe_ingredient",
        sa.Column("recipe_ingredient_id", sa.INTEGER(), nullable=False),
        sa.Column("recipe_id", sa.INTEGER(), nullable=False),
        sa.Column("ingredient_id", sa.INTEGER(), nullable=False),
        sa.Column("unit_id", sa.INTEGER(), nullable=False),
        sa.Column("amount", sa.NUMERIC(), nullable=True),
        sa.Column("sort", sa.SMALLINT(), nullable=True),
        sa.ForeignKeyConstraint(
            ["ingredient_id"],
            ["ingredient.ingredient_id"],
            name=op.f("recipe_ingredient_ingredient_id_fkey"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["recipe_id"],
            ["recipe.recipe_id"],
            name=op.f("recipe_ingredient_recipe_id_fkey"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["unit_id"], ["unit.unit_id"], name=op.f("recipe_ingredient_unit_id_fkey")
        ),
        sa.PrimaryKeyConstraint(
            "recipe_ingredient_id", name=op.f("recipe_ingredient_pkey")
        ),
    )


def downgrade() -> None:
    """Downgrade the database to a previous version."""
    op.drop_table("recipe_ingredient")
    op.drop_table("unit")
    op.drop_table("recipe")
    op.drop_table("ingredient")
