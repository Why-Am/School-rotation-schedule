'''
TODO: 
- add more commandline functionality, such as being able to pass in a specific day if wanted/skip around weeks
'''

from datetime import date, timedelta
import sys

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = 0, 1, 2, 3, 4, 5, 6
DAY = ('ABCDE', 'FGABC', 'DEFGA', 'BCDEF', 'GABCD', 'EFGAB', 'CDEFG')

def get_mondays_date():
    today = date.today()
    current_weekday = today.weekday()

    if current_weekday == MONDAY:
        return today

    elif MONDAY < current_weekday <= THURSDAY:
        return today - timedelta(days=current_weekday) # reference last monday

    elif current_weekday >= FRIDAY:
        return today + timedelta(days=(7 - current_weekday)) # reference next monday

def parse_line(file):
    a = file.readline()
    if a == '':
        print('Blank line reached. Ending.')
        sys.exit(1)
    weekday, formatted_date, schedule_day = a.split(',')

    try:
        return weekday, formatted_date, int(schedule_day)
    except ValueError:
        return weekday, formatted_date, schedule_day.rstrip()
    


monday = get_mondays_date()
assert(monday.weekday() == MONDAY)

try:
    with open(sys.argv[1], 'r') as file:
        while True:
            weekday, formatted_date, schedule_day = parse_line(file)

            if weekday == 'Mon':
                m, d, y = map(int, formatted_date.split('/'))

                if date(month=m, day=d, year=int(f'20{y}')) == monday:
                    break

        print(f'Week of {formatted_date}')
        for _ in range(5):
            try:
                print(weekday, schedule_day, DAY[schedule_day - 1])
            except TypeError:
                print(weekday, schedule_day)
            weekday, formatted_date, schedule_day = parse_line(file)

except FileNotFoundError:
    print('File not found')
