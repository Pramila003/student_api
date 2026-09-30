from fastapi import FastAPI
from database import Base, engine
from schema import StudentSchema
import model

Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
def home():
    return {"mesaage":"student mamangemet api "}

@app.get("/student")
def get_student(student:StudentSchema):
    return {"message":"here we will get all stduent ", "data":student}
