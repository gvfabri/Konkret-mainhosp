"""Recreate missing migration

Revision ID: da2aa9635edf
Revises: 7f7d27b92252
Create Date: 2024-11-23 23:02:56.031230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da2aa9635edf'
down_revision: Union[str, None] = '7f7d27b92252'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
