"""Add Post table

Revision ID: 6cbd634eef26
Revises: de8c45f2cb72
Create Date: 2023-11-23 06:36:22.290884

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from app.post.models import Type


# revision identifiers, used by Alembic.
revision = '6cbd634eef26'
down_revision = 'de8c45f2cb72'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'post',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('text', sa.String(), nullable=True),
        sa.Column('image', sa.String(), nullable=True, default='postdefault.jpg'),
        sa.Column('created', sa.DateTime(), nullable=True, default=datetime.now),
        sa.Column('type', sa.Enum(Type), nullable=True, default='news'),
        sa.Column('enabled', sa.Boolean(), nullable=True, default=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('post')
