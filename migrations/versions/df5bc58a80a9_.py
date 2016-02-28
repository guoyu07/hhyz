"""empty message

Revision ID: df5bc58a80a9
Revises: 6b8c059e47c2
Create Date: 2016-02-27 10:29:02.876115

"""

# revision identifiers, used by Alembic.
revision = 'df5bc58a80a9'
down_revision = '6b8c059e47c2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temp_avatar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=255), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('path')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temp_avatar')
    ### end Alembic commands ###
