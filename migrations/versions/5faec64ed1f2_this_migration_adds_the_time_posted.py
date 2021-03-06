"""This migration adds the time posted

Revision ID: 5faec64ed1f2
Revises: acc15c7c5fd4
Create Date: 2018-11-19 10:13:21.003706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5faec64ed1f2'
down_revision = 'acc15c7c5fd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'posted')
    # ### end Alembic commands ###
