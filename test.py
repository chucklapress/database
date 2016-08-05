import psycopg2

connection = psycopg2.connect("dbname=football_quarter user=dbperson")
cursor = connection.cursor()


def all_info():
    search = input('Need the info')
    cursor.execute("select * from quarterback_stat ;",(search ))
    result = cursor.fetchall()
    print(result)

def player_name_search():
    search = input('search for player by full name ')
    cursor.execute("select * from quarterback_stat where full_name = %s;", (search, ))
    result = cursor.fetchall()
    print(result)

def team_search():
    search = input('List the teams ')
    cursor.execute("select * from quarterback_stat where team_name = %s;",(search))
    result = cursor.fetchall()
    print(result)

def completion_search():
    search = input('List the completion numbers')
    cursor.execute("select full_name, complete from quarterback_stat order by complete;",(search))
    result = cursor.fetchall()
    print(result)

def attempt_search():
    search = input('search player by attempt numbers')
    cursor.execute("select full_name, attempt from quarterback_stat order by attempt;",(search))
    result = cursor.fetchall()
    print(result)

def attempt_percentage_search():
    search = input('search player by attempt percentage')
    cursor.execute("select full_name, att_pct from quarterback_stat order by att_pct;",(search))
    result = cursor.fetchall()
    print(result)

def add_player():
    full_name = input('enter your players full name ')
    team_name = input('enter your players team as an abbrevation ')
    complete = input('enter your players completion number ')
    attempt = input('enter your players attempt numbers ')
    att_pct = input('enter your players attempt to completion percentage ')

    cursor.execute("INSERT INTO quarterback_stat VALUES(%s, %s, %s, %s, %s );" , (full_name, team_name, complete, attempt, att_pct))
    connection.commit()
    print('your player has been added to the database')






#all_info()
#team_search()
#completion_search()
#attempt_search()
#attempt_percentage_search()
player_name_search()
#add_player()
