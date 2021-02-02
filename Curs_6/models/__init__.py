from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TIMESTAMP, INTEGER
from sqlalchemy.sql import func
from sqlalchemy import Column

# Every models shall inherit this class.
DeclarativeBase = declarative_base()


class BaseModel:
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.now())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
