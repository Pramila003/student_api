from fastapi import FastAPI,Depends, status
from database import Base, engine
from sqlalchemy.orm import Session
from schema import StudentSchema, ReponseSchema
import model
import crud
from database import get_db
from typing import List


Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
def home():
    return {"mesaage":"student mamangemet api "}

@app.post("/create_stud",status_code=status.HTTP_201_CREATED)
def create_stud(body: StudentSchema, db:Session=Depends(get_db)):
    return crud.create_stud(body, db) 

@app.get("/get_all", response_model=List[ReponseSchema], status_code=status.HTTP_200_OK)
def get_all(db:Session=Depends(get_db)):
    return crud.get_all(db)


@app.get("/get_one_stud/{stud_id}", response_model=ReponseSchema, status_code=status.HTTP_200_OK)
def get_one_stud(stud_id: int, db:Session=Depends(get_db)):
    return crud.get_one_stud(stud_id, db)
