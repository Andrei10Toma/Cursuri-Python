import tkinter
from app.gui.common import WhiteFrame
from handlers.database import DatabaseHandler
from models.employers import Employee


class EmployeeRow(WhiteFrame):
    def __init__(self, employer, user, master, **kwargs):
        super().__init__(master, **kwargs)
        self.employer = employer
        self.user = user
        self.btn_action = None
        self.first_name_label = None

    @property
    def is_hired(self):
        return len(self.user.employees) > 0

    def hire(self):
        print('hire', self.employer, self.user)
        session = DatabaseHandler.session
        employee = Employee(
            user=self.user,
            employer=self.employer,
            wage=100
        )
        session.add(employee)
        session.commit()
        self.draw()

    def fire(self):
        session = DatabaseHandler.session
        session.delete(self.user.employees[0])
        session.commit()
        self.draw()

    def draw(self):
        if self.first_name_label is None:
            self.first_name_label = tkinter.Label(self, text=self.user.first_name)
            self.first_name_label.pack(side=tkinter.LEFT)

        text = "Fire" if self.is_hired else "Hire"
        command = self.fire if self.is_hired else self.hire

        if self.btn_action is not None:
            self.btn_action.pack_forget()
        self.btn_action = tkinter.Button(self, text=text, command=command)
        self.btn_action.pack(side=tkinter.LEFT)


class EmployeeFrame(WhiteFrame):
    def __init__(self, employer, users, master, **kwargs):
        super().__init__(master, **kwargs)

        self.employer = employer
        self.users = users

    def draw(self):
        for user in self.users:
            employee_row = EmployeeRow(self.employer, user, self)
            employee_row.pack(side=tkinter.TOP)
            employee_row.draw()
