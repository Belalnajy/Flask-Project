"""empty message

Revision ID: d1c2632f9355
Revises: a45a9e5b542a
Create Date: 2025-03-12 13:41:49.286346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1c2632f9355'
down_revision = 'a45a9e5b542a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('discount_price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('discount_price', sa.FLOAT(), nullable=True))

    # ### end Alembic commands ###
