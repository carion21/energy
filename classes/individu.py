
from pydantic import BaseModel

class Individu(BaseModel):
    groupname: str
    upfront: int
    unlock: int
    gender: str
    age: int
    occupation: str
    langue: str
    region: str
   
    