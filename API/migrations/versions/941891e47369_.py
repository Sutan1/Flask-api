"""empty message

Revision ID: 941891e47369
Revises: 5d40e599af52
Create Date: 2024-10-30 21:33:58.859483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '941891e47369'
down_revision = '5d40e599af52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
