from flask import Flask, render_template, jsonify, json, request
import json, sqlite3

app = Flask(__name__)

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
    # print(request.args.get('time'))
    # print(request.args.get('date'))
    # print(request.args.get('game'))
    # print(request.args.get('tot_time'))
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

if __name__ == "__main__":
    app.run(port=1234, debug=True)