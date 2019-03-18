
def sql_setup():
    import sqlite3
    conn= sqlite3.connect("todo.db")
    conn.execute('''CREATE TABLE TODO_TABLE
        (NAME TEXT PRIMARY KEY  NOT NULL,
        DESC CHAR(50) NOT NULL,
        PRIORITY INT NOT NULL,
        ETA TEXT NOT NULL,
        STATUS INT NOT NULL);''')
    print 'Table created successfully'
    conn.commit()
    conn.close()





def sql_insert(name, desc, pri, eta, status):
    import sqlite3
    conn= sqlite3.connect("todo.db")
    conn.execute('''INSERT INTO TODO_TABLE(NAME, DESC, PRIORITY, ETA, STATUS)
        VALUES( ?, ?, ?, ? , ?);''', (name, desc, pri, eta, status) )
    print 'Table insert successfully'
    conn.commit()
    conn.close()

sql_setup()
sql_insert('Design', "TDL project design", 2, "2 hours", 3)
sql_insert('Coding', "Python learning and coding", 2, "1.5 man days", 2)
sql_insert('sending code', "To email", 2, "03/07/2019", 1)
