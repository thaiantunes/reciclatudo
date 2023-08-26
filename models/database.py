from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from .data_model import Base

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://USERNAME:PASSWORD@HOST/DATABASE"
SQLALCHEMY_DATABASE_URL = "mariadb+pymysql://root@localhost/reciclatudo"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = Base.metadata
metadata.create_all(engine)

@contextmanager
def db_session():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()