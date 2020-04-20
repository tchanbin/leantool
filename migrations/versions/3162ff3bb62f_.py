"""empty message

Revision ID: 3162ff3bb62f
Revises: 6c2c69c5d692
Create Date: 2020-04-16 19:45:13.292181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3162ff3bb62f'
down_revision = '6c2c69c5d692'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('houses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('company', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('user', sa.String(length=15), nullable=True),
    sa.Column('house', sa.String(length=15), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('car_procedure_infos_ibfk_3', 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint('car_procedure_infos_ibfk_5', 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint('car_procedure_infos_ibfk_1', 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint('car_procedure_infos_ibfk_2', 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint('car_procedure_infos_ibfk_4', 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint('car_procedure_infos_ibfk_6', 'car_procedure_infos', type_='foreignkey')
    op.create_foreign_key(None, 'car_procedure_infos', 'users', ['second_approval'], ['id'])
    op.create_foreign_key(None, 'car_procedure_infos', 'car_lists', ['car_id'], ['id'])
    op.create_foreign_key(None, 'car_procedure_infos', 'users', ['first_approval'], ['id'])
    op.create_foreign_key(None, 'car_procedure_infos', 'users', ['confirmer'], ['id'])
    op.create_foreign_key(None, 'car_procedure_infos', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'car_procedure_infos', 'procedure_lists', ['procedure_list_id'], ['id'])
    op.drop_constraint('users_ibfk_1', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_ibfk_1', 'users', 'roles', ['role_id'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.drop_constraint(None, 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint(None, 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint(None, 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint(None, 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint(None, 'car_procedure_infos', type_='foreignkey')
    op.drop_constraint(None, 'car_procedure_infos', type_='foreignkey')
    op.create_foreign_key('car_procedure_infos_ibfk_6', 'car_procedure_infos', 'users', ['confirmer'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('car_procedure_infos_ibfk_4', 'car_procedure_infos', 'procedure_lists', ['procedure_list_id'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('car_procedure_infos_ibfk_2', 'car_procedure_infos', 'users', ['user_id'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('car_procedure_infos_ibfk_1', 'car_procedure_infos', 'users', ['first_approval'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('car_procedure_infos_ibfk_5', 'car_procedure_infos', 'users', ['second_approval'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('car_procedure_infos_ibfk_3', 'car_procedure_infos', 'car_lists', ['car_id'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.drop_table('orders')
    op.drop_table('houses')
    # ### end Alembic commands ###
