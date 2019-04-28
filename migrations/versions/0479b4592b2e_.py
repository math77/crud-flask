"""empty message

Revision ID: 0479b4592b2e
Revises: fe67f29c1f59
Create Date: 2019-04-27 20:52:02.050516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0479b4592b2e'
down_revision = 'fe67f29c1f59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ReceitaIngrediente',
    sa.Column('id_receita', sa.Integer(), nullable=False),
    sa.Column('id_ingrediente', sa.Integer(), nullable=False),
    sa.Column('porcentagem', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_ingrediente'], ['Ingrediente.id'], ),
    sa.ForeignKeyConstraint(['id_receita'], ['Receita.id'], ),
    sa.PrimaryKeyConstraint('id_receita', 'id_ingrediente')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ReceitaIngrediente')
    # ### end Alembic commands ###