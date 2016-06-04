import psycopg2
connection = psycopg2.connect("dbname=football_quarter user=dbperson")
cursor = connection.cursor()


cursor.execute("select * from football_stat;")
results = cursor.fetchall()

#results = cursor.fetchall()
#print(results)

#for row in results:
    #print(row[3])


"""for row in results:
    teams =()
    print(row[1])
for row in results:
    name =()
    print(row[0])
for row in results:
    completions =()
    print(row[2])
for row in results:
    attempts =()
    print(row[3])
for row in results:
    attempt_percentage =()
    print(row[4])"""

cursor.execute("select full_name from football_stat where att_pct > 50;")
#cursor.execute("select * from football_stat where attempt > 2 ;")
print(cursor.fetchall())




cursor.close()
connection.close()
