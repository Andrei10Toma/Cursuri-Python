import tkinter


class WhiteFrame(tkinter.Frame):
    def __init__(self, master, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#fff"

        super().__init__(master, kwargs)
