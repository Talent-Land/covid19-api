import pyodbc
import pandas as pd

def database_connection(sql):

# Data Base Info
    server = 'sarumantl.database.windows.net'
    database = 'covid_vaccines_research'
    username = 'sarumancovidvaccines'
    password = 'weareanawesometeam2022#'
# driver= '{SQL Server}'
    driver= '{ODBC Driver 17 for SQL Server}'

# Conection to DataBase
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()



# cursor.execute('SELECT ID')
    # sql = "SELECT * FROM study_type"

    cursor.execute(sql)
    data = cursor.fetchall()


# Create DataFrame
# data = pd.DataFrame(data)
    data = pd.read_sql(sql, cnxn)

# Close Connection
    cursor.close()
    cnxn.close()

    return data
