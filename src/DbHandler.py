import psycopg2
from pathlib import Path
import ConfigReader as dbconfigreader
from datetime import datetime


def add_data_point(roomid=0, humidity=0.0,temperature=0.0):
    _postgres_params = dbconfigreader.config_reader( 'database.ini', 'postgresql')
    conn = psycopg2.connect(dbname=_postgres_params['database'], dbname=_postgres_params['database'],user=_postgres_params['user'], password=_postgres_params['password'])
    curr = conn.cursor()
    date_now = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M")
    print(date_now,time_now)
    # curr.execute('INSERT INTO public.room_condition(roomid,"time",temperature,humidity,room_name,date) VALUES (%s,%s,%s,%s,%s,%s)',(1,'20:38:40',21.1,50.5,'2020-06-14'))
    curr.execute('INSERT INTO public.room_condition(roomid,"time",temperature,humidity, "date") VALUES (%s,%s,%s,%s,%s)',\
    (roomid,time_now,temperature,humidity,date_now))
    conn.commit()
    conn.close()

if __name__ == '__main__':
   add_data_point()