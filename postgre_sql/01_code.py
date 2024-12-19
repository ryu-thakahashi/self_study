# [PostgreSQL driver for Python — Psycopg](https://www.psycopg.org/)

import psycopg2
from icecream import ic

conn = psycopg2.connect("dbname=test user=postgres host=localhost password=postgres")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
cur.execute("SELECT * FROM test;")
ic(cur.fetchone())
