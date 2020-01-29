import flask

# How to create website
app = flask.Flask('MyApp')


@app.errorhandler(404)
def errorPage(err):
    return 'The page you want to visit does not exists.'


@app.route('/')
def indexPage():
    return 'Welcome'


@app.route('/about')
def aboutPage():
    return '<b>This is about </b>'


@app.route('/login')
def loginPage():
    return '''<b>This is Login Page</b><form action='/verify' method='post'>
    Username:<input type='text' name='uname'/><br>
    Password:<input type='password' name='pw'/><br>
    <input type='submit' value='LOGIN' />'''


@app.route('/verify', methods=['POST'])  # method should match in both like get or post
def verifyPage():
    u = flask.request.form['uname']
    p = flask.request.form['pw']
    if not u == 'abc' and p == 'xyz':
        return '<b>Login Failed </b>'
    else:
        import sqlite3
        con = sqlite3.connect('myDB.sqlite3')
        cur = con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result = cur.fetchall()
        return flask.render_template('report.html', res=result)


@app.route('/download/<filename>')
def staticFile(filename):
    return flask.send_from_directory(directory=r'C:\Users\lab365\Desktop\python\bin', filename=filename)


@app.route('/empid/<int:eid>')
def empId(eid):
    D = {'Name': 'abc', 'EMP_ID': eid}
    return D


@app.route('/nameid')
def nameId(nid):
    return str(nid)


@app.route('/logdata')
def logdata():
    return flask.redirect('/login')


@app.route('/passwords')
def passwords():
    return flask.abort(201, 'Access DeniedX')


app.run(host='192.168.3.198', port=8080)

# HTTP METHOD
# 1 GET 2 POST FOR CREATE ACCOUNT 3 PUT FOR UPDATE 4 DELETE
# HTML file in case of bottle framework is .tpl and with Flask is .html and with django is .html
# Template_Path is where u keep the html file
# Inside html file we can write python code too and the execution of that python code will be taken care by Templete Engine
# Templete engine for bottle,flask and django are STE(Simple templete engine),JINJA2,DTE(django tempelete engine
# Start a python statement with %statement in bottle
# Start a python statement with {%statement} in flask
# Start a python statement with {%statement} in django
# In html file indendadtion cannot be maintained thus we use
# %end in bottle and {%endfor%} in flask and django
# variable is written as {{var}} in all
