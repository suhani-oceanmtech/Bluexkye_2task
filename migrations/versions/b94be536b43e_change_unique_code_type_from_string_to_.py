"""change unique_code type from string to float

Revision ID: b94be536b43e
Revises: fc4793ab5737
Create Date: 2024-05-27 17:08:38.085818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b94be536b43e'
down_revision: Union[str, None] = 'fc4793ab5737'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
