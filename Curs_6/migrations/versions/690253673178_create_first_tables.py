"""create first tables

Revision ID: 690253673178
Revises: 
Create Date: 2020-12-23 21:19:52.046454

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '690253673178'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employers',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=225), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=225), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=225), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=225), nullable=False),
    sa.Column('age', mysql.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('employees',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', mysql.INTEGER(), nullable=True),
    sa.Column('employer_id', mysql.INTEGER(), nullable=True),
    sa.Column('wage', mysql.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['employer_id'], ['employers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    op.drop_table('users')
    op.drop_table('employers')
    # ### end Alembic commands ###
