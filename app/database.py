from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


engine=create_engine(settings.database_url)
session=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

def get_db():
    db=session()
    try:
       yield db
    finally:
        db.close()
