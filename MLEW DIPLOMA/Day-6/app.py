from flask import Flask,render_template,request,session
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://krishna:1234567890@diploma.1v5g6.mongodb.net/")
database=cluster['diploma']
collection=database['users']

app=Flask(__name__)
app.secret_key="krishna"

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


@app.route('/uprofile')
def uprofile():
    return render_template("userprofile.html",user=None)

@app.route('/userprofile',methods=['post'])
def userprofile():
    fullname=request.form['fullname']
    user=collection.find_one({"fullname":fullname})
    return render_template("userprofile.html",user=user)

@app.route("/userprofile")
def uprf():
    fullname=request.args.get('fullname')
    user=collection.find_one({"fullname":fullname})
    return render_template("userprofile.html",user=user)

@app.route("/teamdetails")
def td():
    users=collection.find()
    return render_template('teamdetails.html',users=users)

@app.route('/loginuser',methods=["post"])
def loginuser():
    username=request.form['username']
    password=request.form['password']
    print(username,password)
    user=collection.find_one({"username":username})
    if not user:
        return render_template('register.html')
    else:
        if user['username']==username and user['password']==password:
            session['username']=username
            return render_template("dashboard.html")
        else:
            return render_template('login.html',status="Incorrect  password")

@app.route("/myprofile")
def myprf():
    user=collection.find_one({"username":session['username']})
    return render_template("profile.html",user=user)

@app.route("/logout")
def logout():
    session['username']=''
    return render_template("login.html")


if __name__=="__main__":
    print("Server started running......")
    app.run(debug=True)