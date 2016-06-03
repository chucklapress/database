import psycopg2

connection = psycopg2.connect("dbname=football_quarter user=dbperson")

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS football_stat")
table_create_command = """CREATE TABLE football_stat (
  full_name varchar(30),
  team varchar(30),
  complete numeric(3),
  attempt numeric(4),
  att_pct numeric(3)
);"""

cursor.execute(table_create_command)
full_name ='Kirk Cousins'
team ='WAS'
complete =29
attempt =46
att_pct =63

cursor.execute("INSERT INTO football_stat VALUES('Cam Newton', 'CAR', 53, 91, 58);")
cursor.execute("INSERT INTO football_stat VALUES('Tom Brady', 'NE', 55, 98, 56);")
cursor.execute("INSERT INTO football_stat VALUES('Carson Palmer', 'ARI', 48, 81, 59);")
cursor.execute("INSERT INTO football_stat VALUES('Ben Roethlisberger', 'PIT', 42, 68, 62);")
cursor.execute("INSERT INTO football_stat VALUES('Peyton Manning', 'DEN', 51, 92, 55);")
cursor.execute("INSERT INTO football_stat VALUES('Russell Wilson', 'SEA', 44, 74, 60);")
cursor.execute("INSERT INTO football_stat VALUES('Aaron Rodgers', 'GB', 45, 80, 56);")
cursor.execute("INSERT INTO football_stat VALUES('Alex Smith', 'KC', 46, 72, 64);")
cursor.execute("INSERT INTO football_stat VALUES (%s, %s, %s, %s, %s);" ,(full_name, team, complete, attempt, att_pct))
connection.commit()

cursor.close()
connection.close()

