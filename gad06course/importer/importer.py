import json
from handlers.database import DatabaseHandler
from models.users import User
from models.employers import Employer


if __name__ == "__main__":
    session = DatabaseHandler.session

    db_users = session.query(User).all()
    if len(db_users) == 0:
        with open('users.json', 'r') as users_file:
            users = json.load(users_file) or []

        for user_data in users:
            user = User(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
            )
            session.add(user)

    db_employers = session.query(Employer).all()
    if len(db_employers) == 0:
        with open('employers.json', 'r') as employers_file:
            employers = json.load(employers_file) or []

        for employer_data in employers:
            employer = Employer(name=employer_data["name"])
            session.add(employer)

    if len(users) > 0 or len(employers) > 0:
        session.commit()
