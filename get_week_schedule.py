'''
TODO: 
- add more commandline functionality, skip around weeks
- refactor
'''

import argparse
from datetime import date, timedelta
import sys

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = 0, 1, 2, 3, 4, 5, 6
DAY = ('ABCDE', 'FGABC', 'DEFGA', 'BCDEF', 'GABCD', 'EFGAB', 'CDEFG')

parser = argparse.ArgumentParser(description='Find the week\'s schedule')

parser.add_argument(
    'filename', 
    help='the file for the full schedule with comma separated values')

parser.add_argument(
    '-d', '--date', 
    help='what date to use, format yyyy-mm-dd (default is today)',
    default=0)

args = parser.parse_args()

def get_mondays_date(today):
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
    

if args.date == 0:
    today = date.today()
else:
    today = map(int, args.date.split('-'))
    today = date(*today)

monday = get_mondays_date(today)
assert(monday.weekday() == MONDAY)

try:
    with open(args.filename, 'r') as file:
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
