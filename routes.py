from flask import Flask, render_template, jsonify, json, request
import json, sqlite3
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)
m=hashlib.md5()

@app.route("/")
@app.route("/home")
def index():
    return "hello world"


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

@app.route("/login", methods = ['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return jsonify(username)

@app.route("/register", methods = ['POST'])
def register():
    username = request.args.get('username')
    password = request.args.get('password')
    company = request.args.get('company')
    m.update(password)
    return jsonify(m.hexdigest())
    # with sqlite3.connect("db/userdata.db") as connection:
    #     connection.cursor().execute('INSERT INTO users (username, password, company) VALUES (?,?,?)', [username, password, company])
    #     connection.commit()

if __name__ == "__main__":
    app.run(port=1234, debug=True)