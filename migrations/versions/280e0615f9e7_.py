"""empty message

Revision ID: 280e0615f9e7
Revises: 34f108d05452
Create Date: 2021-10-22 12:06:08.564584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '280e0615f9e7'
down_revision = '34f108d05452'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('test', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tests_pkey')
    )
    # ### end Alembic commands ###
