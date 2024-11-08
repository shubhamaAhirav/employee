from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    position: str
    salary: float
    department: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
