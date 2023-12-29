"""posts table

Revision ID: d842caa7df4a
Revises: 
Create Date: 2023-12-29 10:21:51.538210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd842caa7df4a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('Posts')
    pass
