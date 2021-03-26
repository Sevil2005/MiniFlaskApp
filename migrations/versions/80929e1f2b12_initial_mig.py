"""Initial mig

Revision ID: 80929e1f2b12
Revises: 
Create Date: 2021-03-26 19:56:02.390092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80929e1f2b12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('slider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('img', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('slider')
    # ### end Alembic commands ###