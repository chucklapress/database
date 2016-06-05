import psycopg2

connection = psycopg2.connect("dbname=football_quarter user=dbperson")
cursor = connection.cursor()


def welcome():
    welcome = input("Welcome to the NFL 2015 Top quarterback data base.\n"
                    "You can (S)earch or you can (A)dd information to the database,choose (Q) to quit: ").lower()

    if welcome == "s":
        search_data()
    elif welcome == "a":
        add_data()
    elif welcome == "q":
         cursor.close()
         connection.close()
         exit()


def search_data():
    search = input("Search by (F)ull_name, (T)eam_name, (C)omplete, (A)ttempt, Att_(P)ct\n").lower()
    if search == "f":
        name_search()
    elif search == "t":
        team_search()
    elif search == "c":
        complete_search()
    elif search == "a":
        attempt_search()
    elif search == "p":
        att_pct_search()
        search_data()
    else:
        print("The data base is currently only capable of searching the given parameters")
        welcome()


def name_search():
    search = input("Enter a Players name to search, eg.Peyton Manning.. ")
    cursor.execute("select * from quarterback_stat where full_name = %s;", (search, ))
    result = cursor.fetchall()
    print(result)
    welcome()


def team_search():
    search = input("Enter a team name to search, eg. SEA, GB, PIT...: ")
    cursor.execute("select * from quarterback_stat where team_name = %s;", (search, ))
    result = cursor.fetchall()
    print(result)
    welcome()


def complete_search():
    cursor.execute("select full_name, complete from quarterback_stat order by complete DESC ;")
    result = cursor.fetchall()
    print(result)
    welcome()


def attempt_search():
    cursor.execute("select full_name, attempt from quarterback_stat order by attempt DESC ;")
    result = cursor.fetchall()
    print(result)
    welcome()


def att_pct_search():
    cursor.execute("select full_name, att_pct from quarterback_stat order by att_pct DESC ;")
    result = cursor.fetchall()
    print(result)
    welcome()


def add_data():
    full_name = input("Enter the player's name: ")
    team_name = input("Enter the team name, example, SEA, GB, ARI: ")
    complete = input("Enter the number completions as a number, example, 25:  ")
    attempt = input("Enter the number of attempted passes as a number, example, 180: ")
    att_pct = input("Enter the number percentage of complete to attempts as a round number, ie 35: ")

    cursor.execute("INSERT INTO quarterback_stat VALUES(%s, %s, %s, %s, %s );" , (full_name, team_name, complete, attempt, att_pct))
    connection.commit()

    print("Your Player data has been added to the database.")

    print("Search your Player by entering Full name in search !!!")

    welcome()




welcome()
