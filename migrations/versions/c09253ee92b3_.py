"""empty message

Revision ID: c09253ee92b3
Revises: 5c2e4e79cac5
Create Date: 2016-02-21 13:14:12.704050

"""

# revision identifiers, used by Alembic.
revision = 'c09253ee92b3'
down_revision = '5c2e4e79cac5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_tag',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    op.add_column(u'posts', sa.Column('comment_num', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'posts', 'comment_num')
    op.drop_table('post_tag')
    op.drop_table('tags')
    ### end Alembic commands ###
