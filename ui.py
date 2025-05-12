from collections.abc import Callable
from tkinter import Tk, ttk, StringVar
from schedule import Schedule


class Ui:
    def __init__(self, schedule: Schedule) -> None:
        self.root = Tk()
        self.root.title("School rotation schedule")
        self.root.geometry("300x200")
        self.schedule = schedule

        self.mainframe = ttk.Frame(self.root, padding="10")
        self.mainframe.grid(column=0, row=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        for i in range(3):
            self.mainframe.columnconfigure(i, weight=1)
            self.mainframe.rowconfigure(i, weight=1)

        self.prev = ttk.Button(
            self.mainframe,
            text="< Previous",
            command=lambda: self.handle_button(self.schedule.show_prev_week),
        )
        self.prev.grid(column=0, row=0, sticky="nw")

        self.next = ttk.Button(
            self.mainframe,
            text="Next >",
            command=lambda: self.handle_button(self.schedule.show_next_week),
        )
        self.next.grid(column=1, row=0, sticky="ne")

        self.today = ttk.Button(
            self.mainframe,
            text="Today",
            command=lambda: self.handle_button(self.schedule.show_todays_week),
        )
        self.today.grid(column=0, row=2, columnspan=2, sticky="s")

        self.text_var = StringVar(value=self.schedule.text)
        self.text = ttk.Label(self.mainframe, textvariable=self.text_var)
        self.text.grid(column=0, row=1, columnspan=2)

    def mainloop(self) -> None:
        self.root.mainloop()

    def handle_button(self, command: Callable[[], None]) -> None:
        command()
        self.text_var.set(self.schedule.text)
