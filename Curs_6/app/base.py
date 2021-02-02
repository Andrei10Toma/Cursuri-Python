import tkinter
from threading import Thread
from handlers.database import get_employer, get_users
from app.gui.employees import EmployeeFrame


class App:
    def __init__(self):
        self.window_frame = tkinter.Tk()
        self.window_frame.geometry("800x650")

        self.loading_label = None
        self.brand_label = None
        self.employer = None
        self.users = None
        self.is_loading = True

        Thread(target=get_employer, kwargs={"callback": self.set_employer}).start()
        Thread(target=get_users, kwargs={"callback": self.set_users}).start()

    def set_users(self, users=None):
        self.users = users
        self.check_loading_status()

    def set_employer(self, employer=None):
        self.employer = employer
        self.check_loading_status()

    def check_loading_status(self):
        if self.is_loading and (self.users is not None and self.employer is not None):
            self.is_loading = False
            self.draw()

    def draw(self):
        if self.is_loading:
            self.loading_label = tkinter.Label(self.window_frame, text="Loading")
            self.loading_label.pack(side=tkinter.TOP)
        else:
            self.loading_label.pack_forget()
            self.brand_label = tkinter.Label(self.window_frame, text=self.employer.name)
            self.brand_label.pack(side=tkinter.TOP)

            employees_frame = EmployeeFrame(self.employer, self.users, self.window_frame)
            employees_frame.pack(side=tkinter.TOP)
            employees_frame.draw()

    def run(self):
        self.draw()
        self.window_frame.mainloop()
