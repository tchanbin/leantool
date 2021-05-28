"""empty message

Revision ID: 3c29a6a6b6f2
Revises: 6f26354115f7
Create Date: 2021-04-24 20:14:40.037271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c29a6a6b6f2'
down_revision = '6f26354115f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s1-data', sa.Column('jjg_Banci', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_Operators', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_SMEDTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_WipLeft', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_WipRight', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_cycleTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_runningTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_upTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('jjg_valueTime', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('s1-data', 'jjg_valueTime')
    op.drop_column('s1-data', 'jjg_upTime')
    op.drop_column('s1-data', 'jjg_runningTime')
    op.drop_column('s1-data', 'jjg_cycleTime')
    op.drop_column('s1-data', 'jjg_WipRight')
    op.drop_column('s1-data', 'jjg_WipLeft')
    op.drop_column('s1-data', 'jjg_SMEDTime')
    op.drop_column('s1-data', 'jjg_Operators')
    op.drop_column('s1-data', 'jjg_Banci')
    # ### end Alembic commands ###