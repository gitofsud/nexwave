
import bottle
#How to create website
app=bottle.Bottle()
#app.run() #Start the web server
@app.error(404)
def errorpage(err):
    return 'You are blocked to access it'

@app.route('/')
def indexpage():
    return 'Welcome'

@app.route('/about')
def aboutpage():
    return '<b>This is about </b>'

@app.route('/login')
def loginpage():
    return '''<b>This is Login Page</b><form action='/verify' method='post'>
    Username:<input type='text' name='uname'/><br>
    Password:<input type='password' name='pw'/><br>
    <input type='submit' value='LOGIN' />'''

@app.route('/verify',method='post')#method should match in both like get or post
def verifypage():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not u=='abc' and p=='xyz':
        return '<b>Login Failed </b>'
    else:
        return '<b>Login Successful </b>'



app.run(host='192.168.3.198',port=8080)


#HTTP METHOD
#1 GET 2 POST FOR CREATE ACCOUNT 3 PUT FOR UPDATE 4 DELETE
#HTML file in case of bottle framework is .tpl and with Flask is .html and with django is .html
#Template_Path is where u keep the html file
#Inside html file we can write python code too and the execution of that python code will be taken care by Templete Engine
#Templete engine for bottle,flask and django are STE(Simple templete engine),JINJA2,DTE(django tempelete engine
#Start a python statement with %statement in bottle
#Start a python statement with {%statement} in flask
#Start a python statement with {%statement} in django
#In html file indendadtion cannot be maintained thus we use
#%end in bottle and {%endfor%} in flask and django
# variable is written as {{var}} in all

