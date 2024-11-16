import psycopg2
import psycopg2.extras

conn = psycopg2.connect(database="postgres", host="localhost", port="5432")
cur = conn.cursor()

cur.close()
conn.close()
