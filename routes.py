from flask import Flask, render_template, jsonify, json, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import flaskhelper

app = Flask(__name__)
app.config['SECRET_KEY'] ='94b351635db94a3b26de70ef855a5850'
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if flaskhelper.userexists(request.args.get('username'), request.args.get('password'))
    return render_template('index.html')


@app.route("/trackablegames")
def sendtrackablegames():
    return jsonify(flaskhelper.getgames())

@app.route("/update", methods = ['POST', 'GET'])
def updatedb():
    
    time = request.args.get('time')
    date = request.args.get('date')
    game = request.args.get('game')
    tot_time = request.args.get('tot_time')
    bayid = request.args.get('bayid')
    
    return jsonify(flaskhelper.updatedatabase(time, date, game, tot_time, bayid))
    

@app.route("/login", methods = ['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    company = request.args.get('company')

    # Build object to send data to the next for data grabbing
    return jsonify(flaskhelper.login(username, password, company))

@app.route("/register", methods = ['POST','GET'])
def register():
    src = request.args.get['src']

    if src == 'register':
        username = request.args.get('username')
        password = request.args.get('password')
        company = request.args.get('company')
        email = request.args.get('email')
        fullname = request.args.get('fullname')
        
        flaskhelper().register(username, password, email, fullname, company)
    elif src == 'checkname':
        return jsonify(flaskhelper.checkname(request.args.get('name')))
    
    return jsonify("hello")

@app.route("/datadump", methods = ['GET'])
def datadump():
    return jsonify(flaskhelper.getdata())

@app.route('/usernamedump', methods=['GET'])
def usernamedump():
   return jsonify(flaskhelper.getusernames())
 
if __name__ == "__main__":
    app.run(debug=True)