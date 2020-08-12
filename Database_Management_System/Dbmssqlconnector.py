import sqlite3


def UseRData():
        con = sqlite3.connect('user.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,UserID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile INTEGER)')
        con.commit()
        con.close()


def addUsrRec(UserID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con = sqlite3.connect('user.db')
        cur = con.cursor()
        cur.execute('INSERT INTO user VALUES(NOT NULL,?,?,?,?,?,?,?,?)',(UserID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close()


def viewData():
        con = sqlite3.connect('user.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM user')
        row = cur.fetchall()
        con.close()
        return row


def deleteRec(id):
        con = sqlite3.connect('user.db')
        cur = con.cursor()
        cur.execute('DELETE FROM user WHERE id=?',(id))
        con.commit()
        con.close()


def searchData(UserID='',Firstname='',Surname='',DoB='',Age='',Gender='',Address='',Mobile=''):
        con = sqlite3.connect('user.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM user WHERE UserID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?',(UserID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        rows = cur.fetchall()
        con.close()
        return rows


def dataUpdate(id,UserID='',Firstname='',Surname='',DoB='',Age='',Gender='',Address='',Mobile=''):
        con = sqlite3.connect('user.db')
        cur = con.cursor()
        cur.execute('UPDATE user SET UserID=?,Firstname=?,Surname=?,DoB=?,Age=?,Gender=?,Address=?,Mobile=? WHERE id=?',(UserID,Firstname,Surname,DoB,Age,Gender,Address,Mobile,id))
        con.commit()
        con.close()


UseRData()
