from flask import Flask, render_template, jsonify, json, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import flaskhelper

app = Flask(__name__)
app.config['SECRET_KEY'] ='94b351635db94a3b26de70ef855a5850'
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    
    return render_template('index.html')

@app.route("/signup", methods=["GET"])
def signup():
    return render_template('signup.html')

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
    

@app.route("/login", methods = ['POST','GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(password)

    if flaskhelper.login(username, password) == None:
        print("login failed")
        return render_template('index.html')

    return "hello"


@app.route("/register", methods = ['GET', 'POST'])
def register():
    src = request.args.get('src')

    if src == 'register':
        username = request.args.get('username')
        password = request.args.get('password')
        company = request.args.get('company')
        email = request.args.get('email')
        fullname = request.args.get('name')
        
        return flaskhelper.register(username, password, email, fullname, company)
        
    elif src == 'checkcompany':
        print("hi")
        return jsonify(flaskhelper.checkcompany(request.args.get('company')))
    
    return "wrong src"

@app.route("/datadump", methods = ['GET'])
def datadump():
    return jsonify(flaskhelper.getdata())

@app.route('/usernamedump', methods=['GET'])
def usernamedump():
   return jsonify(flaskhelper.getusernames())
 
if __name__ == "__main__":
    app.run(debug=True)