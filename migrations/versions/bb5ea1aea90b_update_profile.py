"""Update profile 

Revision ID: bb5ea1aea90b
Revises: 303b1e36fbc9
Create Date: 2020-09-21 23:44:41.628000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb5ea1aea90b'
down_revision = '303b1e36fbc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_users_username', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.drop_table('profile_photos')
    # ### end Alembic commands ###
