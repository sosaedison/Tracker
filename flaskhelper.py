import json, sqlite3, hashlib

def checkname(name):
    try:
        with sqlite3.connect("db/userdata.db") as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM user_data WHERE fullname=?', [name])
            return cursor.fetchall()
    except Exception as ex:
        print(ex)
        return False

def login(username, psswrd, company):
    password = hashlib.md5(bytes(password,'utf-8'))
    password = password.hexdigest()
    try:
        with sqlite3.connect("db/userdata.db") as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username=? AND psswrd=?', [username, password])
            return cursor.fetchall()
    except Exception as ex:
        print(ex)
        return False

def register(username, psswrd, email, fullname, company):
    psswrd = hashlib.md5(bytes(psswrd,'utf-8')) 
    psswrd = psswrd.hexdigest()
    try:
        with sqlite3.connect("db/userdata.db") as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO user_data (fullname, email, username, psswrd, company) VALUES (?,?,?,?,?)', [fullname, email, username, psswrd, company])
            connection.commit()
            return 'updated!'
    except Exception as ex:
        print(ex)
        return False

def getgames():
    try:
        with open('server_config.json','r') as settings_file:
            settings = json.load(settings_file)
            return settings
    except Exception as ex:
        print(ex)
        return False

def updatedatabase(time, date, game, tot_time, bayid):
    try:
        with sqlite3.connect("db/voxel.db") as connection:
            connection.cursor().execute('INSERT INTO data (game, date, time, time_played, bayid) VALUES (?,?,?,?,?)',[data['game'], data['date'], data['time'], data['tot_time'], data['bayid']])
            connection.commit()
            return "updated!"
    except Exception as ex:
        print(ex)
        return False

def getusernames():
    try:
        with sqlite3.connect("db/userdata.db") as connection:
            curs = connection.cursor()
            curs.execute('SELECT username FROM user_data')
            return curs.fetchall()
    except Exception as ex:
        print(ex)

def getdata():
    try:
        with sqlite3.connect("db/voxel.db") as connection:
            curs = connection.cursor()
            curs.execute("SELECT * FROM voxel_data")
            return curs.fetchall()
    except Exception as ex:
        print(ex)