"""Create users table

Revision ID: f957ae1cfdd5
Revises: 48217206c8f3
Create Date: 2026-04-02 13:26:03.787339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f957ae1cfdd5'
down_revision: Union[str, Sequence[str], None] = '48217206c8f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
