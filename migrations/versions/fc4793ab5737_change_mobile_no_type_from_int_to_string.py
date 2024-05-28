"""change mobile_no type from int to string

Revision ID: fc4793ab5737
Revises: a8faba389950
Create Date: 2024-05-27 17:07:58.702555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc4793ab5737'
down_revision: Union[str, None] = 'a8faba389950'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
