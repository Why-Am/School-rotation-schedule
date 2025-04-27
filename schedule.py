class Schedule:
    def __init__(self, filename):
        self.schedule = []
        with open(filename, 'r') as file:
            line = file.readline()
            line = line.split(',')
            assert len(line) == 3

            self.schedule.append(Day(*line))
    
    def get_week(self):
        print('asdf')
    
    def prev_week(self):
        print('prev')
    
    def next_week(self):
        print('next')

class Day:
    def __init__(self, weekday, datestring, event):
        self.weekday = weekday
        self.datestring = datestring
        self.event = event