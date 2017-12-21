"""stack-request-coltypechange.

Revision ID: 813f9a704eb7
Revises: 47f4ce1e8d75
Create Date: 2016-07-25 11:56:47.705420

"""

# revision identifiers, used by Alembic.
revision = '813f9a704eb7'
down_revision = '47f4ce1e8d75'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    """Upgrade the database to a newer revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.alter_column('stack_analyses_request', 'requestJson',
                    existing_type=postgresql.JSONB(),
                    type_=sa.String(length=4096),
                    existing_nullable=False)
    # end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.alter_column('stack_analyses_request', 'requestJson',
                    existing_type=sa.String(length=4096),
                    type_=postgresql.JSONB(),
                    existing_nullable=False)
    # end Alembic commands ###
