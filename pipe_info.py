import psycopg2

connection = psycopg2.connect("dbname=pipe_collection user=dbperson")
cursor = connection.cursor()

def welcome():
    welcome = input('Welcome to the pipe database it will allow you to search by\n (p)ipe maker, (m)aker_country, (c)ost,(v)endor_name and vendor_(n)umber,\n It also will all you to A(d)d a pipes information, To end simply (q)uit  ')
    if welcome == 'p':
        pipe_makers_name_search()
    elif welcome == 'm':
        pipe_makers_country_search()
    elif welcome == 'c':
        cost_search()
    elif welcome =='v':
        vendor_name_search()
    elif welcome =='n':
        vendor_number_search()
    elif welcome =='d':
        add_pipe_info()
    elif welcome =='q':
        end_program()

def all_info():
    search = input('Press enter for the complete current contents of data base ')
    cursor.execute("select * from smoking_pipes ;",(search ))
    result = cursor.fetchall()
    print(result)

def pipe_makers_name_search():
    search = input('search for pipe maker by full name ')
    cursor.execute("select * from smoking_pipes where maker_name = %s;", (search, ))
    result = cursor.fetchall()
    print(result)
    welcome()

def pipe_makers_country_search():
    search = input('search by pipe makers country by three letter abbrevation ')
    cursor.execute("select * from smoking_pipes where maker_country = %s;", (search, ))
    result = cursor.fetchall()
    print(result)
    welcome()

def cost_search():
    search = input('press enter for a grouping of costs by maker_country')
    cursor.execute("select maker_name, cost from smoking_pipes order by cost;",(search))
    result = cursor.fetchall()
    print(result)
    welcome()

def vendor_name_search():
    search = input('press enter for a grouping of vendors for the makers')
    cursor.execute("select maker_name, vendor_name from smoking_pipes order by vendor_name;",(search))
    result = cursor.fetchall()
    print(result)
    welcome()

def vendor_number_search():
    search = input('press enter for a grouping of pipes by vendor number')
    cursor.execute("select maker_name, vendor_number from smoking_pipes order by vendor_number;",(search))
    result = cursor.fetchall()
    print(result)
    welcome()

def add_pipe_info():
    print('Please enter the following information to add a pipe to the database')
    maker_name = input('enter your makers full name: ')
    maker_country = input('enter your makers country as an abbrevation: ')
    cost = input('enter the makers average pipe cost: ')
    vendor_name = input('enter your pipes vendor name:  ')
    vendor_number = input('enter your pipes vendor number: ')

    cursor.execute("INSERT INTO smoking_pipes VALUES(%s, %s, %s, %s, %s );" , (maker_name, maker_country, cost, vendor_name, vendor_number))
    connection.commit()
    print('your pipe information has been added to the database')
    welcome()

def end_program():
    cursor.close()
    connection.close()
    quit()






welcome()
