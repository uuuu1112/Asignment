from flask import Flask,request,redirect
from flask import render_template,session

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/signin" ,methods=["POST"])
def signin():
    session['name']=request.form["n"]
    session['key']=request.form["k"]
    if session['name']=="test" and session['key']=="test":
        return redirect("/member")
    else:
        return redirect("/error")


@app.route("/signout")
def signout():
    session.pop('name', None)
    session.pop('key', None)
    return redirect("/")

@app.route("/member")
def member():
    if 'name' not in session or 'key' not in session:
        return redirect("/")
    elif session['name']=="test" and session['key']=="test":
        return render_template("member.html")
    
    else:
        return redirect("/")
    


app.run(port=3000) 
