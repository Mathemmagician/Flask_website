"""empty message

Revision ID: 8f318dbdbd9f
Revises: 69abc09325fa
Create Date: 2021-01-06 21:56:04.386438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f318dbdbd9f'
down_revision = '69abc09325fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('info', sa.Text(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goat')
    # ### end Alembic commands ###