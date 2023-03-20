import datetime as dt
from datesCreation import *


class WorkDays():
    
    def __init__(self):
        self.start_date = get_start_date()
        self.date_end = get_end_date()
        self.holidays = get_holidays()

    def get_workdays_list(self, workdays):
        delta_time1 = dt.timedelta(days=1)
        workdays_list = []
        weekdays = ['Понедельник', 'Вторник',
                    'Среда', 'Четверг', 'Пятница', 'Суббота']
        self.start_date -= delta_time1
        while self.start_date != self.date_end:
            self.start_date += delta_time1
            con_1 = self.start_date.weekday() in workdays.keys()
            con_2 = self.start_date not in self.holidays
            if con_1 and con_2:
                for _ in range(int(workdays[self.start_date.weekday()])):
                    workdays_list.append(
                        (weekdays[self.start_date.weekday()], self.start_date.strftime('%d.%m')))
        return workdays_list
