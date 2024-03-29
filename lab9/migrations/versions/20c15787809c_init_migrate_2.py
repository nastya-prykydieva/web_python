"""init migrate 2

Revision ID: 20c15787809c
Revises: 111c53fcd430
Create Date: 2023-11-12 22:24:36.793027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20c15787809c'
down_revision = '111c53fcd430'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedback', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.String(length=500), nullable=True))
        batch_op.drop_column('message')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedback', schema=None) as batch_op:
        batch_op.add_column(sa.Column('message', sa.VARCHAR(length=500), nullable=True))
        batch_op.drop_column('text')

    # ### end Alembic commands ###
