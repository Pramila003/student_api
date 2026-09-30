from pydantic import BaseModel

class StudentSchema(BaseModel):
    name : str
    email : str
    age : int 
    department : str 