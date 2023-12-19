"""init migrate for lab 11_4

Revision ID: b82ea1322ecf
Revises: cdb7f0105429
Create Date: 2023-11-28 04:30:44.692645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b82ea1322ecf'
down_revision = 'cdb7f0105429'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tag',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.drop_table('post_tags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.Column('tag_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.drop_table('post_tag')
    # ### end Alembic commands ###
