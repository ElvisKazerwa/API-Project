"""add content column to post table

Revision ID: 8eed2f9b44e1
Revises: d842caa7df4a
Create Date: 2023-12-29 10:44:04.429164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8eed2f9b44e1'
down_revision: Union[str, None] = 'd842caa7df4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('Posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('Posts', 'content')
    pass
