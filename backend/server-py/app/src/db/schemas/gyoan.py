from .base import Base, TimestampMixin
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

class Gyoan(Base, TimestampMixin):
    __tablename__ = 'gyoan'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(200), nullable=False)
    type = sa.Column(sa.Enum('img_word', 'read', 'write', 'motion', name='gyoan_type'), nullable=False)
    data = sa.Column(pg.JSONB, nullable=True)  # 교안 타입별 스크립트
    # data 구조:
    # {
    #   "script": ["가이드라인1", "가이드라인2", "가이드라인3"],
    #   "파일_경로": "path/to/files"
    # }
    default_words = sa.Column(pg.JSONB, nullable=True)  # 교안 생성 시 포함되는 기초 단어
    # default_words 구조:
    # [
    #   {"word": "단어1", "img": "이미지경로1", "sound": "소리경로1"},
    #   {"word": "단어2", "img": "이미지경로2", "sound": "소리경로2"}
    # ]
