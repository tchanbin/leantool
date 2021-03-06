"""empty message

Revision ID: 00b45450ef7b
Revises: 486765c44fe8
Create Date: 2021-04-28 20:57:14.625897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00b45450ef7b'
down_revision = '486765c44fe8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s1-data', sa.Column('fy_WipLeft', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('fy_WipRight', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('s1-data', 'fy_WipRight')
    op.drop_column('s1-data', 'fy_WipLeft')
    # ### end Alembic commands ###
