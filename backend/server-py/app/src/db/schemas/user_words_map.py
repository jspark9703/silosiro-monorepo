from .base import Base, TimestampMixin
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

class UserWordsMap(Base, TimestampMixin):
    __tablename__ = 'user_words_map'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    words_id = sa.Column(sa.Integer, sa.ForeignKey('words.id'), nullable=False)
    data = sa.Column(pg.JSONB, nullable=True)  # 비공개 단어 목록
    # data 구조:
    # {
    #   "non_visible_word": ["비공개단어1", "비공개단어2", "비공개단어3"]
    # }
