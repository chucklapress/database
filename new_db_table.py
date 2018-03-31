import psycopg2

connection = psycopg2.connect("dbname=pipe_collection user=dbperson")

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS smoking_pipes")
table_create_command = """CREATE TABLE smoking_pipes (
  maker_name varchar(30),
  maker_country varchar(30),
  cost numeric(10),
  vendor_name varchar(30),
  vendor_number numeric(3)
);"""

cursor.execute(table_create_command)
maker_name ='J Alan'
maker_country ='USA'
cost =1200
vendor_name = 'smoking pipes'
vendor_number =1

cursor.execute("INSERT INTO smoking_pipes VALUES('Tom Eltang', 'DEN', 1100, 'smoking pipes', 1);")
cursor.execute("INSERT INTO smoking_pipes VALUES('Ping Zang', 'CHI', 900, 'scandpipes', 2);")
cursor.execute("INSERT INTO smoking_pipes VALUES('Jonas Rosengren', 'SWE', 1000, 'scandpipes', 2);")
cursor.execute("INSERT INTO smoking_pipes VALUES('Konstantin Shekita', 'UKR', 2000, 'scandpipes', 2);")
cursor.execute("INSERT INTO smoking_pipes VALUES('Alex Florov', 'USA', 1800, 'smoking pipes', 1);")
cursor.execute("INSERT INTO smoking_pipes VALUES('Minoru Nagata', 'JPN', 600, 'scandpipes', 2);")
cursor.execute("INSERT INTO smoking_pipes VALUES('Scott Klein', 'USA', 1000, 'smoking pipes', 1);")
cursor.execute("INSERT INTO smoking_pipes VALUES('Stanislav Kamensky', 'RUS', 1300, 'scandpipes', 2);")
cursor.execute("INSERT INTO smoking_pipes VALUES (%s, %s, %s, %s, %s);" ,(maker_name, maker_country, cost, vendor_name, vendor_number))
connection.commit()

cursor.close()
connection.close()
