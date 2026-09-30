from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DB_CONNECTION="postgresql://postgres:pramila2709@localhost:5432/postgres"
DB_CONNECTION="postgresql+psycopg2://postgres:pramila2709@localhost:5432/student_db"

engine = create_engine(DB_CONNECTION)
Base =  declarative_base()
localSession = sessionmaker(bind=engine)

def get_db():
        session =localSession()
        try:
                yield session
        finally:
                session.close()

                