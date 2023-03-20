import datetime as dt
import sqlite3 as sq


def get_start_date():
    con = sq.connect('db/dates.db')
    with con:
        data = con.execute("SELECT start FROM dates").fetchone()
    start_date = dt.date(*[int(i) for i in data[0].split('-')])
    print('Начальная дата получена')
    return start_date


def get_end_date():
    con = sq.connect('db/dates.db')
    with con:
        data = con.execute("SELECT end FROM dates").fetchone()
    date_end = dt.date(*[int(i) for i in data[0].split('-')])
    print('Заключительная дата получена')
    return date_end


def get_holidays():
    holidays = set()
    con = sq.connect('db/dates.db')
    with con:
        data = con.execute("SELECT holiday FROM holidays").fetchall()
    for value in data:
        if value[0] is not None:
            holidays.add(dt.date(*[int(i) for i in value[0].split('-')]))
    print('Даты выходных получены')
    return holidays


def set_start_date(selected_date):
    con = sq.connect('db/dates.db')
    with con:
        con.execute("UPDATE dates SET start = ?", (selected_date,))
    print('Данные начальной даты обновлены')


def set_end_date(selected_date):
    con = sq.connect('db/dates.db')
    with con:
        con.execute("UPDATE dates SET end = ?", (selected_date,))
    print('Данные заключительной даты обновлены')


def set_holidays(selected_dates):
    con = sq.connect('db/dates.db')
    with con:
        data = con.execute("SELECT holiday FROM holidays").fetchall()
    holidays = set()
    for value in data:
        if value[0] is not None:
            holidays.add(dt.date(*[int(i) for i in value[0].split('-')]))
    print('данные получены')
    for value in selected_dates:
        holidays.add(value)
    data = list((i,) for i in holidays)
    with con:
        con.execute('DELETE FROM HOLIDAYS')
    with con:
        sql = 'INSERT INTO holidays (holiday) values(?)'
        con.executemany(sql, data)
    print('Данные о выходных изменены')


def clear_holidays():
    con = sq.connect('db/dates.db')
    with con:
        con.execute('DELETE FROM HOLIDAYS')
    print('Выходные очищены')
