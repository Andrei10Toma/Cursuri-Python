from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER
from sqlalchemy.orm import relationship
from models import DeclarativeBase, BaseModel
from models.users import User


class Employer(DeclarativeBase, BaseModel):
    __tablename__ = 'employers'
    name = Column(VARCHAR(225), nullable=False)
    employees = relationship("Employee")


class Employee(DeclarativeBase, BaseModel):
    __tablename__ = 'employees'
    user_id = Column(INTEGER, ForeignKey(User.id))
    user = relationship(User)
    employer_id = Column(INTEGER, ForeignKey(Employer.id))
    employer = relationship(Employer)
    wage = Column(INTEGER, default=10)
