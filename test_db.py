from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# 1. Database URL (Make sure username, password, and db name match)
DB_CONNECTION = "postgresql+psycopg2://postgres:pramila2709@localhost:5432/student_db"

engine = create_engine(DB_CONNECTION, echo=True)  # echo=True prints SQL queries
Base = declarative_base()

# 2. Define the Model
class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    department = Column(String)

# 3. Create Tables
if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done! Table created successfully.")