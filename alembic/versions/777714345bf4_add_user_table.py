"""add user table

Revision ID: 777714345bf4
Revises: 8eed2f9b44e1
Create Date: 2023-12-29 10:50:38.756230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '777714345bf4'
down_revision: Union[str, None] = '8eed2f9b44e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users', 
                    sa.column('id', sa.Integers(), nullable=False), sa.column('email', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.column('password', sa.String(), nullable=False),sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
