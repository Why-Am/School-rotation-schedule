from datetime import date, timedelta

import pygame as pg

from ui_constants import WIDTH, HEIGHT


class Schedule:
    def __init__(self, filename: str) -> None:
        self.schedule: list[Day] = []
        self.monday: date = self.get_nearest_monday(date.today())
        self.font = pg.font.Font(None, 24)

        with open(filename, "r") as file:
            for line in file.readlines():
                line = line.split(",")
                assert len(line) == 3

                self.schedule.append(Day(*line))

        self.show_todays_week()

    def update_text(self) -> None:
        self.text = ""
        for i in range(5):
            day = self.schedule[self.current_index + i]
            self.text += f"{day.month}/{day.day} {day.weekday}: {day.event}\n"

    def show_todays_week(self) -> None:
        for i in range(len(self.schedule)):
            if (
                self.monday.month == self.schedule[i].month
                and self.monday.day == self.schedule[i].day
            ):
                self.today_index = i
                self.current_index = i

        self.update_text()

    def get_nearest_monday(self, today: date) -> date:
        if today.weekday() < 5:
            return today - timedelta(days=today.weekday())
        else:  # goes to next week if it's the weekend
            return today + timedelta(days=7 - today.weekday())

    def show_prev_week(self) -> None:  # TODO
        print("prev")

        self.update_text()

    def show_next_week(self) -> None:  # TODO
        print("next")

        self.update_text()

    def draw_text(self) -> None:  # TODO
        self.text_surface = self.font.render(self.text, True, "black")
        self.text_rect = self.text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))


class Day:
    def __init__(self, weekday: str, datestring: str, event: str) -> None:
        self.weekday = self.get_weekday(weekday)
        date_parts = datestring.split("/")
        assert len(date_parts) == 3
        self.month = int(date_parts[0])
        self.day = int(date_parts[1])
        self.event = event.rstrip()  # Get rid of the newline

    def get_weekday(self, weekday: str) -> int:
        match weekday.lower():
            case "mon":
                return 0
            case "tue":
                return 1
            case "wed":
                return 2
            case "thu":
                return 3
            case "fri":
                return 4
            # case 'sat': # Hope not
            #     return 5
            # case 'sun': # Hope not
            #     return 6
            case _:
                raise Exception(f'Error: did not find matching weekday for "{weekday}"')
