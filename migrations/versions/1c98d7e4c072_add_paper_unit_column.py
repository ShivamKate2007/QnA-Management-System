"""Add paper_unit column

Revision ID: 1c98d7e4c072
Revises: 8a27f880eee0
Create Date: 2025-04-13 10:54:37.429725

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1c98d7e4c072'
down_revision = '8a27f880eee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('paper_unit', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('set_code', sa.String(length=10), nullable=False))
        batch_op.drop_column('unit')
        batch_op.drop_column('paper')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('paper', mysql.VARCHAR(collation='utf8mb4_general_ci', length=10), nullable=False))
        batch_op.add_column(sa.Column('unit', mysql.VARCHAR(collation='utf8mb4_general_ci', length=50), nullable=False))
        batch_op.drop_column('set_code')
        batch_op.drop_column('paper_unit')

    # ### end Alembic commands ###
