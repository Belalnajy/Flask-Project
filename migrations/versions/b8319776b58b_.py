"""empty message

Revision ID: b8319776b58b
Revises: fe7a466bc67e
Create Date: 2025-03-12 20:53:41.657809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8319776b58b'
down_revision = 'fe7a466bc67e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
