"""init

Revision ID: 956fcb48e62b
Revises: 
Create Date: 2017-10-16 18:36:46.112616

"""
import alembic
import sqlalchemy


# revision identifiers, used by Alembic.
revision = '956fcb48e62b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    alembic.op.create_table(
        'user',
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column('name', sqlalchemy.String(50)),
    )

def downgrade():
    alembic.op.drop_table('user')
