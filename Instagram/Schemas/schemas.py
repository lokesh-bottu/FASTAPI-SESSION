from pydantic import BaseModel

class User(BaseModel):
    Name:str
    Email:str
    Location:str
    Company:str
