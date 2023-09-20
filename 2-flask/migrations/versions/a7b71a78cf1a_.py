"""empty message

Revision ID: a7b71a78cf1a
Revises: de12fd2a2357
Create Date: 2023-09-19 13:02:13.029196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7b71a78cf1a'
down_revision = 'de12fd2a2357'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('programs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('instructor_id', sa.String(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_programs_instructor_id_instructors'), 'instructors', ['instructor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('programs', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_programs_instructor_id_instructors'), type_='foreignkey')
        batch_op.drop_column('instructor_id')

    # ### end Alembic commands ###
