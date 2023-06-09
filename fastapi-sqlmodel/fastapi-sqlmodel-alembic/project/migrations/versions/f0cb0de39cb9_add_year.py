"""add year

Revision ID: f0cb0de39cb9
Revises: fa7f1c02bd78
Create Date: 2023-03-15 12:56:20.541154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0cb0de39cb9'
down_revision = 'fa7f1c02bd78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('year', sa.Integer(), nullable=True))
    # op.alter_column('song', 'id',
    #            existing_type=sa.INTEGER(),
    #            nullable=True,
    #            autoincrement=True)
    op.create_index(op.f('ix_song_year'), 'song', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_song_year'), table_name='song')
    op.alter_column('song', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_column('song', 'year')
    # ### end Alembic commands ###
