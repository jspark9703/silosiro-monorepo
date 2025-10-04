from .base import Base, TimestampMixin
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

class UserMap(Base, TimestampMixin):
    __tablename__ = 'user_map'
    id = sa.Column(sa.Integer, primary_key=True)
    user1_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    user2_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    relation = sa.Column(sa.String(50), nullable=False)  # 환자-보호자 관계
    data = sa.Column(pg.JSONB, nullable=True)  # 공유 정보
    # data 구조:
    # {
    #   "words": [...],
    #   "images": [...],
    #   "목표": ["깡총", "차근"],
    #   "level": "상|중|하",
    #   "point": 0,
    #   "gem": 0,
    #   "badges": [...],
    #   "보유한_아이템": [...],
    #   "현재_장착_중인_아이템": [...]
    # }
