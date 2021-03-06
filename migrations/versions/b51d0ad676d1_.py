"""empty message

Revision ID: b51d0ad676d1
Revises: 
Create Date: 2021-04-16 15:23:47.149152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51d0ad676d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('s1-data',
    sa.Column('openid', sa.String(length=60), nullable=False),
    sa.Column('first_section', sa.String(length=15), nullable=True),
    sa.Column('cy_cycleTime', sa.Integer(), nullable=True),
    sa.Column('cy_SMEDTime', sa.Integer(), nullable=True),
    sa.Column('cy_Operators', sa.Integer(), nullable=True),
    sa.Column('cy_EPE', sa.Integer(), nullable=True),
    sa.Column('cy_runningTime', sa.Integer(), nullable=True),
    sa.Column('cy_Wip', sa.Integer(), nullable=True),
    sa.Column('cy_valueTime', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('openid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('s1-data')
    # ### end Alembic commands ###
