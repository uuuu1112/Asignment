import mysql.connector
from flask import Flask,request,redirect
from flask import render_template,session
myresult1=[] #帳號字串
myresult2=[] #帳號密碼字串



mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="uu12542365",
    database="mydatabase"
)
mycursor=mydb.cursor()


app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup" ,methods=["POST"])
def signup():
    mycursor.execute("select * from customers")
    myresult=mycursor.fetchall()
    for user in myresult:
        myresult1.append(user[1])
    if request.form["upname"] in myresult1:
        return redirect("/error?message=帳號已經被註冊")
    else:
        sql="insert into customers(name,username,password) values (%s,%s,%s)"
        val=(request.form["name"],request.form["upname"],request.form["upkey"])
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect("/")

@app.route("/signin" ,methods=["POST"])
def signin():
    mycursor.execute("select * from customers")
    myresult=mycursor.fetchall()
    for user in myresult:
        myresult2.append([user[1],user[2]])
    if [request.form["inname"],request.form["inkey"]] in myresult2:
        session['iname']=request.form["inname"]
        session['ikey']=request.form["inkey"]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/signout")
def signout():
    session.pop('iname', None)
    session.pop('ikey', None)
    return redirect("/")

@app.route("/member")
def member():
    mycursor.execute("select * from customers")
    myresult=mycursor.fetchall()
    for user in myresult:
        myresult2.append([user[1],user[2]])
    if 'iname' not in session or 'ikey' not in session:
        return redirect("/")
    elif [session['iname'],session['ikey']] in myresult2:
        for user in myresult:
            if session['iname']==user[1] and session['ikey']==user[2]:
                return render_template("member.html",name=user[0])
    else:
        return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html",condition=request.args.get("message","自訂的錯誤訊息"))


app.run(port=3000,debug=True) 
