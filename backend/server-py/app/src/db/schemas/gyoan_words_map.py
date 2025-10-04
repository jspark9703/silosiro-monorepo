from .base import Base, TimestampMixin
import sqlalchemy as sa

class GyoanWordsMap(Base, TimestampMixin):
    __tablename__ = 'gyoan_words_map'
    id = sa.Column(sa.Integer, primary_key=True)
    gyoan_id = sa.Column(sa.Integer, sa.ForeignKey('gyoan.id'), nullable=False)
    words_id = sa.Column(sa.Integer, sa.ForeignKey('words.id'), nullable=False)
