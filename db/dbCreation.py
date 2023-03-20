import sqlite3 as sq
import datetime as dt


class myDB():
    def __init__(self):
        self.con = sq.connect('db/dates.db')

    def create_table(self):
        with self.con:
            # получаем количество таблиц с нужным нам именем
            data = self.con.execute(
                "select count(*) from sqlite_master where type='table' and name='dates'")
            for row in data:
                # если таких таблиц нет
                if row[0] == 0:

                    # создаём таблицу для товаров
                    with self.con:
                        self.con.execute("""
                            CREATE TABLE dates (
                                start DATE,
                                end DATE
                            );
                        """)
                    with self.con:
                        sql = 'INSERT INTO dates (start, end) values(?, ?)'
                        data = (dt.date(2023, 1, 1), dt.date(2023, 12, 31))
                        self.con.execute(sql, data)
                    with self.con:
                        self.con.execute("""
                            CREATE TABLE holidays (
                                holiday DATE
                            );
                        """)
                    with self.con:
                        sql = 'INSERT INTO holidays (holiday) values(?)'
                        data = (dt.date(2023, 1, 1),)
                        self.con.execute(sql, data)
