"""Add seating chart foreign key to student desk

Revision ID: 9de918123dd3
Revises: 1253e20833cd
Create Date: 2025-03-24 11:55:23.783872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '9de918123dd3'
down_revision: Union[str, None] = '1253e20833cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('class', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    op.alter_column('class', 'school_year',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=9),
               existing_nullable=True)
    op.alter_column('class_subject', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    op.alter_column('group_meeting', 'time',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=5),
               existing_nullable=True)
    op.alter_column('group_meeting', 'minutes',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=2),
               existing_nullable=True)
    op.alter_column('school', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    op.alter_column('standard', 'grade',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=50),
               existing_nullable=True)
    op.alter_column('student_class', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    op.add_column('student_desk', sa.Column('seating_chart_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'student_desk', 'seating_chart', ['seating_chart_id'], ['id'])
    op.alter_column('student_note', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    op.alter_column('subject', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    op.alter_column('team', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    op.alter_column('unit', 'color',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=10),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('unit', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('team', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('subject', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('student_note', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.drop_constraint(None, 'student_desk', type_='foreignkey')
    op.drop_column('student_desk', 'seating_chart_id')
    op.alter_column('student_class', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('standard', 'grade',
               existing_type=sa.Text(length=50),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('school', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('group_meeting', 'minutes',
               existing_type=sa.Text(length=2),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('group_meeting', 'time',
               existing_type=sa.Text(length=5),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('class_subject', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('class', 'school_year',
               existing_type=sa.Text(length=9),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    op.alter_column('class', 'color',
               existing_type=sa.Text(length=10),
               type_=mysql.TINYTEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###
