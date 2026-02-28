from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    role: str

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True




class TaskCreate(BaseModel):
    title: str
    employee_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    employee_id: int

    class Config:
        from_attributes = True


class TaskStatusUpdate(BaseModel):
    status: str


class IssueCreate(BaseModel):
    description: str
    task_id: int

class IssueResponse(BaseModel):
    id: int
    description: str
    task_id: int

    class Config:
        from_attributes = True



