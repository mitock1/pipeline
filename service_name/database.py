from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker

from .config import get_config

config = get_config()
SQLALCHEMY_DATABASE_URL = config.SQLALCHEMY_DATABASE_URI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    **config.SQLALCHEMY_ENGINE_OPTIONS
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@event.listens_for(engine, "engine_connect")
def receive_engine_connect(conn, branch):
    conn.connection.setencoding("utf-8")


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()
