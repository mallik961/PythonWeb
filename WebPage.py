from flask import Flask,request,render_template,jsonify
import json
import urllib.request
import sqlite3
from  registeredvalues import logincred

#conn = sqlite3.connect(':memory:')



# cur.execute("""CREATE TABLE logintablenew(
#                 username text,
#                 password text)""")




#
# conn = sqlite3.connect('login.db')
# cur = conn.cursor()



#cur.execute("DELETE FROM logintablenew")

# cur.execute("SELECT * FROM logintablenew")
# print(cur.fetchall())
#
# conn.commit()
#
# conn.close()

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])


def index(user = None):
    if user != None:
        # text_box_value = request.GET['username']

     return render_template("MyHtml.html",user = user)
    else:
     return render_template("Login.html",user = user)

@app.route('/login', methods=['GET','POST'])

def login():

    # usernamereg = request.form['username1']
    # passwordreg = request.form['password']
    # emailreg = request.form['email']
    # confirm_passwordreg = request.form['confirm_password']
    #
    # print(usernamereg)
    # print(emailreg)
    # print(passwordreg)
    # print(confirm_passwordreg)


    conn = sqlite3.connect('registration.db')

    cur = conn.cursor()

    # cur.execute("""CREATE TABLE registration(
    #                       username text,
    #                        password text,
    #                        email text)""")


    #cur.execute("DELETE FROM registration")

    cur.execute("SELECT * FROM registration")
    print(cur.fetchall())

    # registration = logincred(usernamereg,passwordreg,emailreg)



    #cur.execute("INSERT INTO registration VALUES(:username,:password,:email)",{'username':registration.uname,'password':registration.password,'email':registration.email})

    conn.commit()
    conn.close()
    return render_template("Login.html")


# def index(user = None):
#
#         return render_template("Login.html",user = user)


@app.route("/bunclick", methods=['POST', 'GET'])
def submit():
    #Moving forward code
    print("hi")
    username = request.form['username']

    password = request.form['password']

    log = logincred(username,password)

    conn = sqlite3.connect('login.db')
    cur = conn.cursor()



    with conn:
        cur.execute("INSERT INTO logintablenew VALUES(:username,:password)",{'username':log.uname,'password':log.password})
        conn.commit()
        # conn.close()




    if username == password:

        return render_template('MyHtml.html',username=username)
    else:
        return render_template("Login.html")



@app.route('/registration', methods=['POST', 'GET'])
def registration():



    return render_template('registration.html')

@app.route('/csscheck')
def csscheck():
    return render_template('csschecking.html')


@app.route('/registertry/<loginname>')
def registertry(loginname = None):
    if loginname != None:
        print("")
        if loginname == "mallik":
            checking = "nee mallik than"
            return jsonify("registered " + loginname + checking)
        return jsonify("registered "+loginname)
    else:
        print("")
        return ("0")

@app.route("/mallik/mallik96",methods=['GET','POST'])
def logincheck():

    loginresult = [
        {
            'login':'success'
        }
    ]

    return jsonify(loginresult)

@app.route("/listcheck")
def listcheck():
    food = ['orange','apple','samosa','kedi']

    articles = [
        {
            'id': 1,
            'title': 'Article One',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'Brad Traversy',
            'create_date': '04-25-2017'
        },
        {
            'id': 2,
            'title': 'Article Two',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'John Doe',
            'create_date': '04-25-2017'
        },
        {
            'id': 3,
            'title': 'Article Three',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'Brad Traversy',
            'create_date': '04-25-2017'
        }
    ]

    return render_template('listcheck.html',food=articles)


@app.route('/testtemp/<name>')

def testtemp(name):
    return render_template("MyHtml.html",name=name)


@app.route('/methods',methods=['GET','POST'])

def methods():
    if request.method == "GET":
        return "GET"
    else:
        return "PSOt"


@app.route('/first')

def first():
    return "<h2>Hello i am second page</h2>"

@app.route('/sec/<name>')

def sec(name):
    return "hi i am %s" % name

@app.route('/POSTid/<int:id>')

def POSTid(id):
    return "hi i am %s" % id

@app.route("/jsontry",methods=['GET','POST'])
def jsontry():
    articles = [
        {
            'id': 11,
            'title': 'Article One',
            #'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'Brad Traversy',
            'create_date': '1-25-2017'
        },
        {
            'id': 21,
            'title': 'Article Two',
            #'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'John Doe',
            'create_date': '2-25-2017'
        },
        {
            'id': 31,
            'title': 'Article Three',
            #'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'Brad Traversy',
            'create_date': '3-25-2017'
        }]


    return jsonify(articles)

app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)

with urllib.request.urlopen("http://127.0.0.1:5000/jsontry") as url:
    data = json.loads(url.read().decode())
    print(data)