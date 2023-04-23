"""Initial migration, created 'topics' and 'messages' tables

Revision ID: 001
Revises: 
Create Date: 2023-04-23 23:49:27.809086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'messages',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('from_chat_id', sa.BIGINT(), nullable=False),
        sa.Column('from_message_id', sa.BIGINT(), nullable=False),
        sa.Column('to_chat_id', sa.BIGINT(), nullable=False),
        sa.Column('to_message_id', sa.BIGINT(), nullable=False),
        sa.Column('incoming', sa.BOOLEAN(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint(
            'from_chat_id', 'from_message_id', 'to_chat_id', 'to_message_id',
            name='unique_messages_ids_combinations'
        )
    )
    op.create_table(
        'topics',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.BIGINT(), nullable=False),
        sa.Column('topic_id', sa.INTEGER(), nullable=False),
        sa.Column('first_message_id', sa.INTEGER(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'topic_id', name='unique_topics_pairs')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('topics')
    op.drop_table('messages')
    # ### end Alembic commands ###