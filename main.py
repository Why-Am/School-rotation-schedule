from ui import Ui
from schedule import Schedule

schedule = Schedule("Q4_schedule.csv")
ui = Ui(schedule)
ui.mainloop()
