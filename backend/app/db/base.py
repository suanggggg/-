from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 这里放置创建表的引用导入（实现留白）
# Ensure models are imported so metadata.create_all() picks them up
from app.models import user, question, assessment  # noqa: F401
