"""Ingredient name unique constraint.

Revision ID: 7c7c869c3566
Revises: 57e0063e0dc0
Create Date: 2023-09-21 17:35:25.911526
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7c7c869c3566"
down_revision: Union[str, None] = "57e0063e0dc0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade the database to a later version."""
    op.create_unique_constraint(op.f("ingredient_name_key"), "ingredient", ["name"])


def downgrade() -> None:
    """Downgrade the database to a previous version."""
    op.drop_constraint(op.f("ingredient_name_key"), "ingredient", type_="unique")
