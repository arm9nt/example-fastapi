"""add content column to post table

Revision ID: cdc236ef1b7a
Revises: 9abedbf9a858
Create Date: 2024-12-30 15:08:35.264173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdc236ef1b7a'
down_revision: Union[str, None] = '9abedbf9a858'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
