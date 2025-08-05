"""add content column to post table

Revision ID: c572c0d607d9
Revises: c19315ded52d
Create Date: 2025-08-05 13:53:29.928825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c572c0d607d9'
down_revision: Union[str, Sequence[str], None] = 'c19315ded52d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False, server_default=''))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
