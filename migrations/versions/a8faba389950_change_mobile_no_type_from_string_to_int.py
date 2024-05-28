"""change mobile_no type from string to int

Revision ID: a8faba389950
Revises: 08a5f14fd981
Create Date: 2024-05-27 17:07:35.479932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8faba389950'
down_revision: Union[str, None] = '08a5f14fd981'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
