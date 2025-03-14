"""Initial migration2

Revision ID: fd295cf055c7
Revises: 831fab5273eb
Create Date: 2025-03-07 21:52:47.796204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd295cf055c7'
down_revision: Union[str, None] = '831fab5273eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('class_subject', sa.Column('color', sa.Text(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('class_subject', 'color')
    # ### end Alembic commands ###
