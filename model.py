from database import Base
from sqlalchemy import Column, Integer, String

class StudentModel(Base):
    __tablename__ = "Students"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    department = Column(String)