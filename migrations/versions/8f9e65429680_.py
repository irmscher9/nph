"""empty message

Revision ID: 8f9e65429680
Revises: 906432a90367
Create Date: 2018-11-13 18:13:58.723414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f9e65429680'
down_revision = '906432a90367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('downvotes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'downvotes')
    # ### end Alembic commands ###
