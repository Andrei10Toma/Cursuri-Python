from models import DeclarativeBase, BaseModel
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER
from sqlalchemy.orm import relationship


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'users'
    first_name = Column(VARCHAR(225), nullable=False)
    last_name = Column(VARCHAR(225), nullable=False)
    email = Column(VARCHAR(225), nullable=False, unique=True)
    age = Column(INTEGER, default=18)
    employees = relationship("Employee")
