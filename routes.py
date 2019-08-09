from flask import Flask, render_template, jsonify, json, request, session, redirect
import json, sqlite3
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)



@app.route("/", methods=["GET", "POST"])
def index():
    # password = 
    # if request.method == 'POST':

    #     session['user'] = request.args.get('username')
    return render_template('login.html')


@app.route("/trackablegames")
def sendtrackablegames():
    with open('server_config.json','r') as settings_file:
        settings = json.load(settings_file)
    print('Sent tracked games to a bay')
    return jsonify(settings)

@app.route("/update", methods = ['POST', 'GET'])
def updatedb():
    
    data = {
        "time": request.args.get('time'),
        "date": request.args.get('date'),
        "game": request.args.get('game'),
        "tot_time": request.args.get('tot_time'),
        "bayid": request.args.get('bayid')
    }
    
    with sqlite3.connect("db/voxel.db") as connection:
        connection.cursor().execute('INSERT INTO data (game, date, time, time_played, bayid) VALUES (?,?,?,?,?)',[data['game'], data['date'], data['time'], data['tot_time'], data['bayid']])
        connection.commit()
    ret = 'hello post'
    return jsonify(ret)

@app.route("/login", methods = ['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    company = 'Voxelvrp'

    password = hashlib.md5(bytes(password,'utf-8'))
    password = password.hexdigest()

    with sqlite3.connect("db/userdata.db") as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND psswrd=?', [username, password])
        return jsonify(cursor.fetchall())

@app.route("/register", methods = ['POST','GET'])
def register():
    username = request.args.get('username')
    password = request.args.get('password')
    company = request.args.get('company')

    hasher = hashlib.md5()
    hasher.update(bytes(password, 'utf-8'))
    passwordhash = hasher.hexdigest()
    
    with sqlite3.connect("db/userdata.db") as connection:
        connection.cursor().execute('INSERT INTO users (username, psswrd, company) VALUES (?,?,?)', [ username, passwordhash, company])
        connection.commit()
        
    return jsonify("hello")

@app.route("/datadump", methods = ['GET'])
def datadump():
    with sqlite3.connect("db/voxel.db") as connection:
        curs = connection.cursor()
        curs.execute("SELECT * FROM voxel_data")
        return jsonify(curs.fetchall())

@app.route('/usernamedump', methods=['GET'])
def usernamedump():
    with sqlite3.connect("db/userdata.db") as connection:
        curs = connection.cursor()
        curs.execute('SELECT username FROM users')
        return jsonify(curs.fetchall())


if __name__ == "__main__":
    app.run(port=1234, debug=True)