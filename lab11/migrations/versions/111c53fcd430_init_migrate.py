"""init migrate

Revision ID: 111c53fcd430
Revises: 
Create Date: 2023-11-12 16:40:57.930648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '111c53fcd430'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
