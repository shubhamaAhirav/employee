from sqlalchemy import Column, Integer, String, Float
from db import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String, index=True)
    salary = Column(Float)
    department = Column(String, nullable=True)