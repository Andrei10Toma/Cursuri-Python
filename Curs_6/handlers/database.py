from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import DB_CONNECTION
from models.employers import Employer
from models.users import User


class DatabaseHandler:
    engine = create_engine(DB_CONNECTION)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()


def get_employer(callback=None):
    sleep(1)
    session = DatabaseHandler.session
    employer = session.query(Employer).first()

    if callback is not None:
        callback(employer)


def get_users(callback=None):
    sleep(1)
    session = DatabaseHandler.session
    users = session.query(User).all()

    if callback is not None:
        callback(users)
