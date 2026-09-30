from schema import StudentSchema
from sqlalchemy.orm import Session
from model import StudentModel
from fastapi import HTTPException


def create_stud(body:StudentSchema, db: Session):
    data = body.model_dump()

    new_stud = StudentModel(name = data["name"], email = data["email"], age = data["age"], department = data["department"])

    db.add(new_stud)
    db.commit()
    db.refresh(new_stud)
    return new_stud

def get_all(db: Session):
    students = db.query(StudentModel).all()
    return students

def get_one_stud(stud_id: int, db:Session):
    student = db.query(StudentModel).get(stud_id)
    if not student:
        raise HTTPException(404, detail={"error code":"invalid stduent id"})
    return student 
