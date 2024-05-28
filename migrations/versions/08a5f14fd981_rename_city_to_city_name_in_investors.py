"""rename city to city_name in investors

Revision ID: 08a5f14fd981
Revises: 452dea2d27c5
Create Date: 2024-05-27 17:03:21.489509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08a5f14fd981'
down_revision: Union[str, None] = '452dea2d27c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
