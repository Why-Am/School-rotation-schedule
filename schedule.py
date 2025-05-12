from datetime import date, timedelta


class Schedule:

    def __init__(self, filename: str) -> None:
        self.schedule: list[Day] = []
        self.beginning_reached = False
        self.end_reached = False

        self.get_nearest_monday()

        with open(filename, "r") as file:
            for line in file.readlines():
                line = line.split(",")
                assert len(line) == 3
                self.schedule.append(Day(*line))

        self.show_todays_week()

    def get_nearest_monday(self) -> None:
        today = date.today()
        if today.weekday() < 5:
            self.monday = today - timedelta(days=today.weekday())
        else:
            self.monday = today + timedelta(days=7 - today.weekday())

    def show_todays_week(self) -> None:
        try:
            self.current_index: int = self.today_index
            self.end_reached = False
            self.beginning_reached = False
            self.update_text()
        except AttributeError:
            for i in range(len(self.schedule)):
                if (
                    self.monday.month == self.schedule[i].month
                    and self.monday.day == self.schedule[i].day
                    and self.monday.year == self.schedule[i].year
                ):
                    self.today_index = i
                    self.current_index = i
                    self.update_text()
                    return
            # Couldn't get today's week
            self.today_index = 0
            self.current_index = 0
            self.update_text()

    def show_prev_week(self) -> None:
        if self.beginning_reached:
            return

        self.end_reached = False

        prev_index = self.current_index

        while True:
            self.current_index -= 1
            if self.current_index < 0:  # Beginning reached
                self.current_index = prev_index
                self.beginning_reached = True
                return
            elif self.schedule[self.current_index].weekday_num == 0:
                self.update_text()
                return

    def show_next_week(self) -> None:
        if self.end_reached:
            return

        self.beginning_reached = False

        prev_index = self.current_index

        while True:
            self.current_index += 1
            if self.current_index >= len(self.schedule):  # End reached
                self.current_index = prev_index
                self.end_reached = True
                return
            elif self.schedule[self.current_index].weekday_num == 0:
                self.update_text()
                return

    def update_text(self) -> None:
        self.text = ""
        try:
            for i in range(5):
                day = self.schedule[self.current_index + i]
                self.text += f"{day.month}/{day.day} {day.weekday_str}: {day.event}\n"
        except IndexError:
            pass
        self.text = self.text.rstrip()


class Day:
    days = ("Mon", "Tue", "Wed", "Thu", "Fri")

    def __init__(self, weekday: str, datestring: str, event: str):
        self.weekday_str = weekday
        self.weekday_num = self.days.index(weekday)
        assert self.weekday_num in (0, 1, 2, 3, 4)

        date_parts = datestring.split("/")
        self.month = int(date_parts[0])
        self.day = int(date_parts[1])
        self.year = int("20" + date_parts[2])
        self.event = event.rstrip()
