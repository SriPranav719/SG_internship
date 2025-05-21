from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from datetime import date

# enum e

# SQlmodels
class User(SQLModel,table=True):

    id : int = Field(primary_key = True)
    name : str
    email: EmailStr
    
    tasks : list["Task"]=Relationship(back_populates = "user")
    
# Task

class Task(SQLModel, table = True):
    
    title : int = Field(primary_key = True)
    description : str
    due_date  : date
    
    user_id : int = Field(foreign_key="user.id")
    
    user : User = Relationship(back_populates = "tasks")
    