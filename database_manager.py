import sqlite3 as sql

def listExtension():
    con = sql.connect(".database/data_source.db")  # Make sure this path is correct
    cur = con.cursor()
    data = cur.execute('SELECT * FROM extension').fetchall()
    con.close()
    return data

def insertContact(email, name):
    con = sql.connect(".database/data_source.db")  # Make sure this path is correct
    cur = con.cursor()
    cur.execute("INSERT INTO contact_list (email,name) VALUES (?,?)", (email,name))
    con.commit()
    con.close()

def is_new_email(email):
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()
    try:
        cur.execute('SELECT COUNT(*) FROM contact_list WHERE email = ?', (email,))
        count = cur.fetchone()[0] == 0
        return is_new
    except:
        return False
    finally:
        con.close()