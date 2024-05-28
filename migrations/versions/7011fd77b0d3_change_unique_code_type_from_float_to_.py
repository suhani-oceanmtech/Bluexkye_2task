"""change unique_code type from float to timestamp

Revision ID: 7011fd77b0d3
Revises: b94be536b43e
Create Date: 2024-05-27 17:08:55.665046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7011fd77b0d3'
down_revision: Union[str, None] = 'b94be536b43e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
