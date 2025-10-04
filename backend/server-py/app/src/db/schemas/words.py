from .base import Base, TimestampMixin
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

class Words(Base, TimestampMixin):
    __tablename__ = 'words'
    id = sa.Column(sa.Integer, primary_key=True)
    gyoan_types = sa.Column(pg.ARRAY(sa.String), nullable=True)  # 단어가 사용될 교안의 유형
    is_img = sa.Column(sa.Boolean, default=False, nullable=False)
    is_sound = sa.Column(sa.Boolean, default=False, nullable=False)
    is_user_gen = sa.Column(sa.Boolean, default=False, nullable=False)  # 유저가 만든 단어인지 여부
    created_by = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)  # user_id
    data = sa.Column(pg.JSONB, nullable=True)  # 단어 데이터
    # data 구조:
    # [
    #   {"word": "단어1", "img": "이미지경로1", "sound": "소리경로1"},
    #   {"word": "단어2", "img": "이미지경로2", "sound": "소리경로2"}
    # ]
