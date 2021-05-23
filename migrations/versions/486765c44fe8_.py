"""empty message

Revision ID: 486765c44fe8
Revises: e7683d7815df
Create Date: 2021-04-28 20:44:31.663449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '486765c44fe8'
down_revision = 'e7683d7815df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s1-data', sa.Column('zp1_Banci', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_Operators', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_SMEDTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_WipLeft', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_WipRight', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_cycleTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_runningTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_upTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp1_valueTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_Banci', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_Operators', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_SMEDTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_WipLeft', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_WipRight', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_cycleTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_runningTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_upTime', sa.Integer(), nullable=True))
    op.add_column('s1-data', sa.Column('zp2_valueTime', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('s1-data', 'zp2_valueTime')
    op.drop_column('s1-data', 'zp2_upTime')
    op.drop_column('s1-data', 'zp2_runningTime')
    op.drop_column('s1-data', 'zp2_cycleTime')
    op.drop_column('s1-data', 'zp2_WipRight')
    op.drop_column('s1-data', 'zp2_WipLeft')
    op.drop_column('s1-data', 'zp2_SMEDTime')
    op.drop_column('s1-data', 'zp2_Operators')
    op.drop_column('s1-data', 'zp2_Banci')
    op.drop_column('s1-data', 'zp1_valueTime')
    op.drop_column('s1-data', 'zp1_upTime')
    op.drop_column('s1-data', 'zp1_runningTime')
    op.drop_column('s1-data', 'zp1_cycleTime')
    op.drop_column('s1-data', 'zp1_WipRight')
    op.drop_column('s1-data', 'zp1_WipLeft')
    op.drop_column('s1-data', 'zp1_SMEDTime')
    op.drop_column('s1-data', 'zp1_Operators')
    op.drop_column('s1-data', 'zp1_Banci')
    # ### end Alembic commands ###
