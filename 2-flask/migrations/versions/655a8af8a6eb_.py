"""empty message

Revision ID: 655a8af8a6eb
Revises: 75c7bb83819a
Create Date: 2023-09-20 20:16:29.043195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '655a8af8a6eb'
down_revision = '75c7bb83819a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('programs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('src', sa.String(), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_programs_src'), ['src'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('programs', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_programs_src'), type_='unique')
        batch_op.drop_column('src')

    # ### end Alembic commands ###