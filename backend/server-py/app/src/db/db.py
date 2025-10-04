
import os
from contextlib import contextmanager
from typing import Generator, Optional
from dotenv import load_dotenv

from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Database:
    def __init__(self, database: Optional[str] = None, echo: bool = False) -> None:
        """Initialize database connection using environment variables from .env file"""
        try:
            # Get database configuration from environment variables
            db_host = os.getenv('DB_HOST', 'localhost')
            db_port = int(os.getenv('DB_PORT', '5432'))
            db_name = database or os.getenv('DB_NAME', 'silosiro_db')
            db_user = os.getenv('DB_USER', 'postgres')
            db_password = os.getenv('DB_PASSWORD', 'password')
            
            # Create database URL
            url = URL.create(
                drivername="postgresql+psycopg2",
                username=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
                database=db_name,
            )
            
            # Create engine with connection pooling
            self.engine = create_engine(
                url, 
                echo=echo,
                pool_pre_ping=True,
                pool_recycle=300
            )
            
            # Create session factory
            self._session_factory = sessionmaker(
                bind=self.engine, 
                autocommit=False, 
                autoflush=False
            )
            
            logger.info(f"Database connection initialized: {db_user}@{db_host}:{db_port}/{db_name}")
            
        except Exception as e:
            logger.error(f"Failed to initialize database connection: {e}")
            raise

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """Get a database session with automatic cleanup"""
        session: Session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Database session error: {e}")
            raise e
        finally:
            session.close()
