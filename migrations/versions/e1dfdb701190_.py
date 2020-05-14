"""empty message

Revision ID: e1dfdb701190
Revises: f7ec1df1de40
Create Date: 2020-05-08 11:22:32.108238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1dfdb701190'
down_revision = 'f7ec1df1de40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car_procedure_infos', sa.Column('current_line_node_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('car_procedure_infos', 'current_line_node_id')
    # ### end Alembic commands ###
