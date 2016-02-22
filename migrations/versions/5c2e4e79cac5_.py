"""empty message

Revision ID: 5c2e4e79cac5
Revises: 45b66ec5b775
Create Date: 2016-02-20 23:41:53.736157

"""

# revision identifiers, used by Alembic.
revision = '5c2e4e79cac5'
down_revision = '45b66ec5b775'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('collect', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'collect')
    ### end Alembic commands ###