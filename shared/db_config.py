from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://<username>:<password>@<rds-endpoint>:3306/<database_name>"

# Create a shared database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Provide a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
