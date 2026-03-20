import psycopg2

conn=psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="qwerty",
        host="localhost",
        port="5432"
        )
print("Connected!")
