from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import and_, desc
from .db import Database
from .schemas.user import User
from .schemas.words import Words
from .schemas.user_words_map import UserWordsMap
from .schemas.progress_log import ProgressLog
import logging

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db: Database):
        self.db = db

    async def create_user(self, user_data: Dict[str, Any]) -> User:
        """사용자 생성"""
        with self.db.session() as session:
            user = User(**user_data)
            session.add(user)
            session.flush()  # Get the ID
            session.refresh(user)
            return user

    async def find_user_by_id(self, user_id: int) -> Optional[User]:
        """사용자 ID로 조회"""
        with self.db.session() as session:
            return session.query(User).filter(User.id == user_id).first()

    async def find_user_by_user_id(self, user_id: str) -> Optional[User]:
        """사용자 ID로 조회 (user_id 필드)"""
        with self.db.session() as session:
            return session.query(User).filter(User.user_id == user_id).first()

    async def find_all_users(self) -> List[User]:
        """모든 사용자 조회"""
        with self.db.session() as session:
            return session.query(User).all()

    async def update_user(self, user_id: int, update_data: Dict[str, Any]) -> Optional[User]:
        """사용자 업데이트"""
        with self.db.session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                for key, value in update_data.items():
                    setattr(user, key, value)
                session.flush()
                session.refresh(user)
                return user
            return None

    async def delete_user(self, user_id: int) -> bool:
        """사용자 삭제"""
        with self.db.session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                return True
            return False


class WordsService:
    def __init__(self, db: Database):
        self.db = db

    async def create_words(self, words_data: Dict[str, Any]) -> Words:
        """단어 생성"""
        with self.db.session() as session:
            words = Words(**words_data)
            session.add(words)
            session.flush()
            session.refresh(words)
            return words

    async def find_words_by_id(self, words_id: int) -> Optional[Words]:
        """단어 조회"""
        with self.db.session() as session:
            return session.query(Words).filter(Words.id == words_id).first()

    async def find_words_by_creator(self, created_by: int) -> List[Words]:
        """사용자가 생성한 단어들 조회"""
        with self.db.session() as session:
            return session.query(Words).filter(Words.created_by == created_by).all()

    async def find_words_with_images(self) -> List[Words]:
        """이미지가 있는 단어들 조회"""
        with self.db.session() as session:
            return session.query(Words).filter(Words.is_img == True).all()

    async def find_words_with_sounds(self) -> List[Words]:
        """소리가 있는 단어들 조회"""
        with self.db.session() as session:
            return session.query(Words).filter(Words.is_sound == True).all()

    async def find_user_generated_words(self) -> List[Words]:
        """사용자가 생성한 단어들 조회"""
        with self.db.session() as session:
            return session.query(Words).filter(Words.is_user_gen == True).all()


class UserWordsMapService:
    def __init__(self, db: Database):
        self.db = db

    async def create_user_words_map(self, user_id: int, words_id: int, data: Optional[Dict[str, Any]] = None) -> UserWordsMap:
        """사용자-단어 매핑 생성"""
        with self.db.session() as session:
            user_words_map = UserWordsMap(
                user_id=user_id,
                words_id=words_id,
                data=data
            )
            session.add(user_words_map)
            session.flush()
            session.refresh(user_words_map)
            return user_words_map

    async def find_user_words_maps_by_user_id(self, user_id: int) -> List[UserWordsMap]:
        """사용자의 단어 매핑 조회"""
        with self.db.session() as session:
            return session.query(UserWordsMap).filter(UserWordsMap.user_id == user_id).all()

    async def find_user_words_map_by_ids(self, user_id: int, words_id: int) -> Optional[UserWordsMap]:
        """특정 사용자와 단어의 매핑 조회"""
        with self.db.session() as session:
            return session.query(UserWordsMap).filter(
                and_(UserWordsMap.user_id == user_id, UserWordsMap.words_id == words_id)
            ).first()

    async def update_user_words_map(self, user_id: int, words_id: int, data: Dict[str, Any]) -> Optional[UserWordsMap]:
        """사용자-단어 매핑 업데이트"""
        with self.db.session() as session:
            user_words_map = session.query(UserWordsMap).filter(
                and_(UserWordsMap.user_id == user_id, UserWordsMap.words_id == words_id)
            ).first()
            if user_words_map:
                user_words_map.data = data
                session.flush()
                session.refresh(user_words_map)
                return user_words_map
            return None

    async def delete_user_words_map(self, user_id: int, words_id: int) -> bool:
        """사용자-단어 매핑 삭제"""
        with self.db.session() as session:
            user_words_map = session.query(UserWordsMap).filter(
                and_(UserWordsMap.user_id == user_id, UserWordsMap.words_id == words_id)
            ).first()
            if user_words_map:
                session.delete(user_words_map)
                return True
            return False


class ProgressLogService:
    def __init__(self, db: Database):
        self.db = db

    async def create_progress_log(self, user_id: int, started_at, log_type: str, data: Optional[Dict[str, Any]] = None) -> ProgressLog:
        """진행 로그 생성"""
        with self.db.session() as session:
            progress_log = ProgressLog(
                user_id=user_id,
                started_at=started_at,
                type=log_type,
                data=data
            )
            session.add(progress_log)
            session.flush()
            session.refresh(progress_log)
            return progress_log

    async def find_progress_logs_by_user_id(self, user_id: int) -> List[ProgressLog]:
        """사용자의 진행 로그 조회"""
        with self.db.session() as session:
            return session.query(ProgressLog).filter(
                ProgressLog.user_id == user_id
            ).order_by(desc(ProgressLog.started_at)).all()

    async def find_progress_log_by_id(self, log_id: int) -> Optional[ProgressLog]:
        """진행 로그 ID로 조회"""
        with self.db.session() as session:
            return session.query(ProgressLog).filter(ProgressLog.id == log_id).first()

    async def update_progress_log(self, log_id: int, data: Dict[str, Any]) -> Optional[ProgressLog]:
        """진행 로그 업데이트"""
        with self.db.session() as session:
            progress_log = session.query(ProgressLog).filter(ProgressLog.id == log_id).first()
            if progress_log:
                progress_log.data = data
                session.flush()
                session.refresh(progress_log)
                return progress_log
            return None

    async def delete_progress_log(self, log_id: int) -> bool:
        """진행 로그 삭제"""
        with self.db.session() as session:
            progress_log = session.query(ProgressLog).filter(ProgressLog.id == log_id).first()
            if progress_log:
                session.delete(progress_log)
                return True
            return False
