"""add foreign-key to posts table

Revision ID: 92a2d811ea38
Revises: 777714345bf4
Create Date: 2023-12-29 11:06:53.659955

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92a2d811ea38'
down_revision: Union[str, None] = '777714345bf4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="iusers", local_cols=['owner_id'], remote_cols=7['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', 'owner_id')
    pass