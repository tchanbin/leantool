"""empty message

Revision ID: 27b1812bf6d8
Revises: 00b45450ef7b
Create Date: 2021-05-08 20:23:09.432245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27b1812bf6d8'
down_revision = '00b45450ef7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s1-data', sa.Column('kh_banCi', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('kh_huoPan', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('kh_totalLeft', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('kh_totalMonth', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('kh_totalRight', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('s1-data', 'kh_totalRight')
    op.drop_column('s1-data', 'kh_totalMonth')
    op.drop_column('s1-data', 'kh_totalLeft')
    op.drop_column('s1-data', 'kh_huoPan')
    op.drop_column('s1-data', 'kh_banCi')
    # ### end Alembic commands ###
