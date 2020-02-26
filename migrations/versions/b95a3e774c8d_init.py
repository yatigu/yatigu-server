"""init

Revision ID: b95a3e774c8d
Revises: 
Create Date: 2020-02-26 16:47:15.122695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b95a3e774c8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test',
        sa.Column('id', sa.Unicode(), nullable=True),
        sa.Column('pw', sa.Unicode(), nullable=True),
        sa.UniqueConstraint('id', 'pw', name=op.f('uq_id_pw'))
    )


def downgrade():
    op.drop_table(
        'test'
    )
