"""Change user to plural and remove all tables

Revision ID: a99b9dd28fbf
Revises: 
Create Date: 2025-03-20 11:59:32.142161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a99b9dd28fbf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class_subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_class_subject_id'), 'class_subject', ['id'], unique=False)
    op.create_table('concept',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_concept_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('description', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['parent_concept_id'], ['concept.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_concept_id'), 'concept', ['id'], unique=False)
    op.create_table('mistake',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mistake', sa.Text(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mistake_id'), 'mistake', ['id'], unique=False)
    op.create_table('school',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('img', sa.Text(length=255), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_school_id'), 'school', ['id'], unique=False)
    op.create_table('standard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Text(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Text(length=255), nullable=True),
    sa.Column('grade', sa.Text(length=50), nullable=True),
    sa.Column('subject', sa.Text(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_standard_id'), 'standard', ['id'], unique=False)
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Text(length=255), nullable=True),
    sa.Column('last_name', sa.Text(length=255), nullable=True),
    sa.Column('birthday', sa.Text(length=255), nullable=True),
    sa.Column('img', sa.Text(length=255), nullable=True),
    sa.Column('grade_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_id'), 'student', ['id'], unique=False)
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subject_id'), 'subject', ['id'], unique=False)
    op.create_table('concept_standard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.Column('standard_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.ForeignKeyConstraint(['standard_id'], ['standard.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_concept_standard_id'), 'concept_standard', ['id'], unique=False)
    op.create_table('student_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(length=255), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_note_id'), 'student_note', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Text(length=255), nullable=True),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('img', sa.Text(length=255), nullable=True),
    sa.Column('email', sa.Text(length=255), nullable=True),
    sa.Column('password', sa.Text(length=255), nullable=True),
    sa.Column('premium', sa.Boolean(), nullable=True),
    sa.Column('school', sa.Integer(), nullable=True),
    sa.Column('bday_notification_day', sa.Text(length=255), nullable=True),
    sa.Column('bday_notification_time', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['school'], ['school.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('grade', sa.JSON(), nullable=True),
    sa.Column('grade_min', sa.Integer(), nullable=True),
    sa.Column('grade_max', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('school_year', sa.Text(length=9), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_class_id'), 'class', ['id'], unique=False)
    op.create_table('layout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.Text(length=255), nullable=True),
    sa.Column('status', sa.Enum('active', 'inactive', 'archived', name='chart_status_enum'), nullable=True),
    sa.Column('rows', sa.Integer(), nullable=True),
    sa.Column('cols', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_layout_id'), 'layout', ['id'], unique=False)
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.Column('team_admin_id', sa.Integer(), nullable=True),
    sa.Column('img', sa.Text(length=255), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.ForeignKeyConstraint(['team_admin_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_id'), 'team', ['id'], unique=False)
    op.create_table('class_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(length=255), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.Text(length=255), nullable=True),
    sa.Column('updated', sa.Text(length=255), nullable=True),
    sa.Column('type', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_class_note_id'), 'class_note', ['id'], unique=False)
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Text(length=255), nullable=True),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('description', sa.Text(length=255), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_id'), 'group', ['id'], unique=False)
    op.create_table('student_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_class_id'), 'student_class', ['id'], unique=False)
    op.create_table('unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('is_premade', sa.Boolean(), nullable=True),
    sa.Column('color', sa.Text(length=10), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_unit_id'), 'unit', ['id'], unique=False)
    op.create_table('user_team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_team_id'), 'user_team', ['id'], unique=False)
    op.create_table('assign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(length=100), nullable=True),
    sa.Column('description', sa.Text(length=100), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Text(length=100), nullable=True),
    sa.Column('date_created', sa.Text(length=100), nullable=True),
    sa.Column('status', sa.Text(length=100), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assign_id'), 'assign', ['id'], unique=False)
    op.create_table('group_concept',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_concept_id'), 'group_concept', ['id'], unique=False)
    op.create_table('group_meeting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Text(length=255), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(length=255), nullable=True),
    sa.Column('created', sa.Text(length=255), nullable=True),
    sa.Column('time', sa.Text(length=5), nullable=True),
    sa.Column('minutes', sa.Text(length=2), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_meeting_id'), 'group_meeting', ['id'], unique=False)
    op.create_table('group_metric',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(length=255), nullable=True),
    sa.Column('description', sa.Text(length=255), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(length=255), nullable=True),
    sa.Column('date', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_metric_id'), 'group_metric', ['id'], unique=False)
    op.create_table('group_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(length=255), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.Text(length=255), nullable=True),
    sa.Column('updated', sa.Text(length=255), nullable=True),
    sa.Column('type', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_note_id'), 'group_note', ['id'], unique=False)
    op.create_table('group_student_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(length=255), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.Text(length=255), nullable=True),
    sa.Column('updated', sa.Text(length=255), nullable=True),
    sa.Column('type', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_student_note_id'), 'group_student_note', ['id'], unique=False)
    op.create_table('metric',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Text(length=255), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(length=255), nullable=True),
    sa.Column('date', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_metric_id'), 'metric', ['id'], unique=False)
    op.create_table('unit_concept',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_unit_concept_id'), 'unit_concept', ['id'], unique=False)
    op.create_table('unit_standard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('standard_id', sa.Integer(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['standard_id'], ['standard.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_unit_standard_id'), 'unit_standard', ['id'], unique=False)
    op.create_table('assign_concept',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.Column('assign_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assign_id'], ['assign.id'], ),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assign_concept_id'), 'assign_concept', ['id'], unique=False)
    op.create_table('assign_result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assign_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('status', sa.Text(length=100), nullable=True),
    sa.Column('retest_score', sa.Integer(), nullable=True),
    sa.Column('retest_status', sa.Text(length=100), nullable=True),
    sa.ForeignKeyConstraint(['assign_id'], ['assign.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_assign_result_id'), 'assign_result', ['id'], unique=False)
    op.create_table('group_meeting_concept',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_meeting_id', sa.Integer(), nullable=True),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.ForeignKeyConstraint(['group_meeting_id'], ['group_meeting.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_meeting_concept_id'), 'group_meeting_concept', ['id'], unique=False)
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(length=255), nullable=True),
    sa.Column('answer', sa.Text(length=255), nullable=True),
    sa.Column('is_multiple_choice', sa.Boolean(), nullable=True),
    sa.Column('assignment_id', sa.Integer(), nullable=True),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assignment_id'], ['assign.id'], ),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_id'), 'question', ['id'], unique=False)
    op.create_table('spiral_concept',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concept_id', sa.Integer(), nullable=True),
    sa.Column('assign_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assign_id'], ['assign.id'], ),
    sa.ForeignKeyConstraint(['concept_id'], ['concept.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_spiral_concept_id'), 'spiral_concept', ['id'], unique=False)
    op.create_table('student_metric',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('metric_id', sa.Integer(), nullable=True),
    sa.Column('mistake_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['metric_id'], ['metric.id'], ),
    sa.ForeignKeyConstraint(['mistake_id'], ['mistake.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_metric_id'), 'student_metric', ['id'], unique=False)
    op.create_table('question_response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('mistake_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(length=255), nullable=True),
    sa.ForeignKeyConstraint(['mistake_id'], ['mistake.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_response_id'), 'question_response', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_response_id'), table_name='question_response')
    op.drop_table('question_response')
    op.drop_index(op.f('ix_student_metric_id'), table_name='student_metric')
    op.drop_table('student_metric')
    op.drop_index(op.f('ix_spiral_concept_id'), table_name='spiral_concept')
    op.drop_table('spiral_concept')
    op.drop_index(op.f('ix_question_id'), table_name='question')
    op.drop_table('question')
    op.drop_index(op.f('ix_group_meeting_concept_id'), table_name='group_meeting_concept')
    op.drop_table('group_meeting_concept')
    op.drop_index(op.f('ix_assign_result_id'), table_name='assign_result')
    op.drop_table('assign_result')
    op.drop_index(op.f('ix_assign_concept_id'), table_name='assign_concept')
    op.drop_table('assign_concept')
    op.drop_index(op.f('ix_unit_standard_id'), table_name='unit_standard')
    op.drop_table('unit_standard')
    op.drop_index(op.f('ix_unit_concept_id'), table_name='unit_concept')
    op.drop_table('unit_concept')
    op.drop_index(op.f('ix_metric_id'), table_name='metric')
    op.drop_table('metric')
    op.drop_index(op.f('ix_group_student_note_id'), table_name='group_student_note')
    op.drop_table('group_student_note')
    op.drop_index(op.f('ix_group_note_id'), table_name='group_note')
    op.drop_table('group_note')
    op.drop_index(op.f('ix_group_metric_id'), table_name='group_metric')
    op.drop_table('group_metric')
    op.drop_index(op.f('ix_group_meeting_id'), table_name='group_meeting')
    op.drop_table('group_meeting')
    op.drop_index(op.f('ix_group_concept_id'), table_name='group_concept')
    op.drop_table('group_concept')
    op.drop_index(op.f('ix_assign_id'), table_name='assign')
    op.drop_table('assign')
    op.drop_index(op.f('ix_user_team_id'), table_name='user_team')
    op.drop_table('user_team')
    op.drop_index(op.f('ix_unit_id'), table_name='unit')
    op.drop_table('unit')
    op.drop_index(op.f('ix_student_class_id'), table_name='student_class')
    op.drop_table('student_class')
    op.drop_index(op.f('ix_group_id'), table_name='group')
    op.drop_table('group')
    op.drop_index(op.f('ix_class_note_id'), table_name='class_note')
    op.drop_table('class_note')
    op.drop_index(op.f('ix_team_id'), table_name='team')
    op.drop_table('team')
    op.drop_index(op.f('ix_layout_id'), table_name='layout')
    op.drop_table('layout')
    op.drop_index(op.f('ix_class_id'), table_name='class')
    op.drop_table('class')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_student_note_id'), table_name='student_note')
    op.drop_table('student_note')
    op.drop_index(op.f('ix_concept_standard_id'), table_name='concept_standard')
    op.drop_table('concept_standard')
    op.drop_index(op.f('ix_subject_id'), table_name='subject')
    op.drop_table('subject')
    op.drop_index(op.f('ix_student_id'), table_name='student')
    op.drop_table('student')
    op.drop_index(op.f('ix_standard_id'), table_name='standard')
    op.drop_table('standard')
    op.drop_index(op.f('ix_school_id'), table_name='school')
    op.drop_table('school')
    op.drop_index(op.f('ix_mistake_id'), table_name='mistake')
    op.drop_table('mistake')
    op.drop_index(op.f('ix_concept_id'), table_name='concept')
    op.drop_table('concept')
    op.drop_index(op.f('ix_class_subject_id'), table_name='class_subject')
    op.drop_table('class_subject')
    # ### end Alembic commands ###
