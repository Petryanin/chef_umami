"""1. Unique constraints.

Revision ID: a4e5498024c3
Revises: 57e0063e0dc0
Create Date: 2023-09-27 17:04:44.429730
"""
from typing import Sequence

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "a4e5498024c3"
down_revision: str | None = "57e0063e0dc0"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade the database to a later version."""
    op.create_unique_constraint(op.f("ingredient_name_key"), "ingredient", ["name"])
    op.create_unique_constraint(op.f("recipe_name_key"), "recipe", ["name"])
    op.drop_constraint(
        "recipe_ingredient_ingredient_id_fkey", "recipe_ingredient", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("recipe_ingredient_ingredient_id_fkey"),
        "recipe_ingredient",
        "ingredient",
        ["ingredient_id"],
        ["ingredient_id"],
    )
    op.create_unique_constraint(op.f("unit_full_name_key"), "unit", ["full_name"])


def downgrade() -> None:
    """Downgrade the database to a previous version."""
    op.drop_constraint(op.f("unit_full_name_key"), "unit", type_="unique")
    op.drop_constraint(
        op.f("recipe_ingredient_ingredient_id_fkey"),
        "recipe_ingredient",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "recipe_ingredient_ingredient_id_fkey",
        "recipe_ingredient",
        "ingredient",
        ["ingredient_id"],
        ["ingredient_id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(op.f("recipe_name_key"), "recipe", type_="unique")
    op.drop_constraint(op.f("ingredient_name_key"), "ingredient", type_="unique")
