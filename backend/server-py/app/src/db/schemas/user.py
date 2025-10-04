from datetime import datetime
from .base import Base, TimestampMixin
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

class User(Base, TimestampMixin):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.String(64), unique=True, nullable=False)
    password = sa.Column(sa.String(128), nullable=False)
    type = sa.Column(sa.Enum('patient', 'caregiver', 'therapist', name='user_type'), nullable=False)
    data = sa.Column(pg.JSONB, nullable=True)  # 부가 정보를 json으로