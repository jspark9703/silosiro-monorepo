from .base import Base, TimestampMixin
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

class ProgressLog(Base, TimestampMixin):
    __tablename__ = 'progress_log'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    started_at = sa.Column(sa.DateTime, nullable=False)
    type = sa.Column(sa.Enum('video_call', 'solo_learning', name='learning_type'), nullable=False)
    data = sa.Column(pg.JSONB, nullable=True)  # 학습 데이터
    # data 구조:
    # {
    #   "목표": ["깡총", "차근"],
    #   "week": 1,
    #   "step": 1,
    #   "data": {
    #     "성공_여부": true,
    #     "progress": 0.8
    #   }
    # }
