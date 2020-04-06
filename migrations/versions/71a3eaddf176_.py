"""empty message

Revision ID: 71a3eaddf176
Revises: 877e7fe6fbbe
Create Date: 2020-04-06 11:24:41.884461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71a3eaddf176'
down_revision = '877e7fe6fbbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('package_procedure_infos', sa.Column('status', sa.String(length=15), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('package_procedure_infos', 'status')
    # ### end Alembic commands ###
