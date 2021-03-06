"""empty message

Revision ID: a09e941336aa
Revises: 823658494b39
Create Date: 2017-05-31 14:14:06.296493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a09e941336aa'
down_revision = '823658494b39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('huntlocation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hunt_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hunt_id'], ['hunts.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('hunt_map')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hunt_map',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('hunt_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('location_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['hunt_id'], ['hunts.id'], name='hunt_map_hunt_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name='hunt_map_location_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='hunt_map_pkey')
    )
    op.drop_table('huntlocation')
    # ### end Alembic commands ###
