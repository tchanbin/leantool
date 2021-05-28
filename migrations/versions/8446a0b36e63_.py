"""empty message

Revision ID: 8446a0b36e63
Revises: 61716484556f
Create Date: 2021-05-13 15:59:05.199532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8446a0b36e63'
down_revision = '61716484556f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s1-data', sa.Column('gys_materialInventory', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('s1-data', 'gys_materialInventory')
    # ### end Alembic commands ###