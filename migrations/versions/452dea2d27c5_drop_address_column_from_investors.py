"""drop address column from investors

Revision ID: 452dea2d27c5
Revises: b1c91fa27c2b
Create Date: 2024-05-27 16:50:51.286838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '452dea2d27c5'
down_revision: Union[str, None] = 'b1c91fa27c2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
