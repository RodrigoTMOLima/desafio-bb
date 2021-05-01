"""init

Revision ID: 06cf8ab3b5d5
Revises: 
Create Date: 2021-04-30 23:59:45.218305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06cf8ab3b5d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(30), nullable=False),
        sa.Column('image', sa.LargeBinary, nullable=False),        
    )


def downgrade():
    op.drop_table('users')
