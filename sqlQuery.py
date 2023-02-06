import pyodbc


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=DERDMPC\SQLEXPRESS;"
                          "Database=wroSkyscrapers;"
                          "Trusted_Connection=yes;")


###Add data to sql###
def addCranesData(x,y,z):
    try:
        cursor = cnxn.cursor()
        cursor.execute('''INSERT INTO craneNumbersWroclaw(postNick,postDate,craneNumbers) 
        VALUES(?, ?, ?)''',(x, y, z))
        cnxn.commit()
    except:
        print("An exception occured")
