"""Initial ref stack support.

Revision ID: 21b3add12b10
Revises: 3eb32f202f93
Create Date: 2016-11-01 12:22:31.092782

"""

# revision identifiers, used by Alembic.
revision = '21b3add12b10'
down_revision = '3eb32f202f93'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    """Upgrade the database to a newer revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.create_table('reference_stacks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('version', sa.String(length=255), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('dependencies', postgresql.JSONB(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name', 'version', name='stack_unique'))
    # end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.drop_table('reference_stacks')
    # end Alembic commands ###
