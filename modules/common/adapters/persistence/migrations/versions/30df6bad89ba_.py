"""empty message

Revision ID: 30df6bad89ba
Revises: b988d80825f2
Create Date: 2024-04-14 01:00:56.615717

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "30df6bad89ba"
down_revision: Union[str, None] = "b988d80825f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "mail",
        sa.Column("mail_id", sa.BigInteger(), nullable=False),
        sa.Column("mail", sa.String(length=50), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("mail_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("mail")
    # ### end Alembic commands ###