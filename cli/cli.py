

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from app.database import SessionLocal
from app import crud, schemas

def menu():
    print("\nEmployee Task Manager CLI")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

def add_employee():
    name = input("Enter employee name: ")
    role = input("Enter employee role: ")
    db = SessionLocal()
    employee = schemas.EmployeeCreate(name=name, role=role)
    crud.create_employee(db, employee)
    db.close()
    print("Employee added successfully!")

def view_employees():
    db = SessionLocal()
    employees = crud.get_employees(db)
    db.close()
    for emp in employees:
        print(f"{emp.id} - {emp.name} ({emp.role})")

while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
