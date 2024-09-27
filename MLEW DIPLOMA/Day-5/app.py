from flask import Flask,render_template,request
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://krishna:1234567890@diploma.1v5g6.mongodb.net/")
database=cluster['diploma']
collection=database['application']

app=Flask(__name__)

@app.route("/")         #default api
def index():
    return render_template('index.html')

@app.route("/login")
def index1():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/name")
def name():
    return render_template('name.html',name="Krishna")

@app.route("/registeruser",methods=['post'])
def registeruser():
    a=request.form['fullname']
    b=request.form['email']
    c=request.form['password']
    # print(fullname,email,password)
    collection.insert_one({
        "fullname":a,
        "email":b,
        "password":c
    })
    return render_template("register.html",status="Data captured")

@app.route('/profile')
def display():
    user=collection.find_one({"fullname":"krishna"})
    return render_template("profile.html",user=user)

if __name__=="__main__":
    print("Server started running......")
    app.run(debug=True)