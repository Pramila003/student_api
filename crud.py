from schema import StudentSchema
from sqlalchemy.orm import Session



def create_stud(body:StudentSchema, db: Session):
    data = body.model_dump()

    new_stud = StudentSchema(name = data["name"], email = data["email"], age = data["age"], department = data["department"])

    db.add(new_stud)
    db.commit()
    db