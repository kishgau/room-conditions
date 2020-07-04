import psycopg2
from pathlib import Path
import ConfigReader as dbconfigreader

postgresParams = dbconfigreader.config( 'database.ini', 'postgresql')
conn = psycopg2.connect(dbname=postgresParams['database'],user=postgresParams['user'], password=postgresParams['password'])
curr = conn.cursor()
curr.execute('INSERT INTO public.room_condition(roomid,"time",temperature,humidity,room_name,date) VALUES (%s,%s,%s,%s,%s,%s)',(1,'20:38:40',21.1,50.5,'MB','2020-06-14'))
conn.commit()
conn.close()

