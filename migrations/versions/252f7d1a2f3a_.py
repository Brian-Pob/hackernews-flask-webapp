"""empty message

Revision ID: 252f7d1a2f3a
Revises: a2340649f4d1
Create Date: 2022-10-19 01:37:18.257671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '252f7d1a2f3a'
down_revision = 'a2340649f4d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('aud', sa.String(length=64), nullable=True))
    op.drop_index('ix_user_username', table_name='user')
    op.create_index(op.f('ix_user_aud'), 'user', ['aud'], unique=True)
    op.drop_column('user', 'username')
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=64), nullable=True))
    op.drop_index(op.f('ix_user_aud'), table_name='user')
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.drop_column('user', 'aud')
    # ### end Alembic commands ###
