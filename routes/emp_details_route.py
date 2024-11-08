from sqlalchemy.orm import Session
import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def delete_employee(db: Session, employee_id: int):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
    return employee

def update_employee(db: Session, employee_id: int, employee_data: schemas.EmployeeCreate):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee:
        for key, value in employee_data.model_dump().items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
    return employee
