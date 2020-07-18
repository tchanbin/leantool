"""empty message

Revision ID: c330e431fb40
Revises: 2131041bb3ed
Create Date: 2020-07-18 15:41:49.387513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c330e431fb40'
down_revision = '2131041bb3ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('procedure_states', sa.Column('procedure_state_approval_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('procedure_states', 'procedure_state_approval_time')
    # ### end Alembic commands ###
