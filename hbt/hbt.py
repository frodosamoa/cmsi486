import json
import Habit
import Day
import Session
import User
import cgi

from bottle import route, get, post, put, debug, run, request, redirect
from bottle import template, static_file, error, response
from pymongo import MongoClient


####
# ROUTES
####

@route('/signup')
def get_signup():
    return template('signup', dict(username='', password='', password_error='',
                                   username_error='', verify_error =''))

@route('/signin')
def get_signin():
    return template('signin', dict(username='', password='', login_error=''))

@route('/')
def get_habits():
    username = check_logged_in()
    l = habits.get_habits(username)
    return template('habits', dict(username=username, myhabits=l))

@route('/newhabit')
def newhabit():
    username = check_logged_in()
    return template('new_habit', dict(username=username, name='', times = '',
                                      occurence='', reminders='', categories=''))

@route('/categories')
def get_categories():
    username = check_logged_in()
    return template('categories', dict(username=username))

@route('/graphs')
def get_graphs():
    username = check_logged_in()
    return template('graphs', dict(username=username))

@route('/logout')
def logout():
    cookie = request.get_cookie("session")
    sessions.end_session(cookie)
    response.set_cookie("session", "")
    redirect("/signin")

####
# POSTS
####

@post('/newhabit')
def post_new_habit():
    username = check_logged_in()
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories').split(',')
    habits.insert_habit(username, name, times, occurence, reminders, categories)

    redirect('/')

@post('/signin')
def signin():
    username = request.forms.get("username")
    password = request.forms.get("password")

    print "user submitted ", username, "pass ", password

    user_record = users.validate_login(username, password)
    if user_record:
        session_id = sessions.begin_session(user_record['_id'])

        if session_id is None:
            redirect("/internal_error")

        cookie = session_id
        response.set_cookie("session", cookie)
        redirect("/")

    else:
        return template("signin", dict(username=cgi.escape(username), password="",
                                    login_error="invalid login"))

@post('/signup')
def signup():
    username = request.forms.get("username")
    password = request.forms.get("password")
    verify = request.forms.get("verify")

    errors = {'username': cgi.escape(username)}
    if users.validate_signup(username, password, verify, errors):

        if not users.add_user(username, password):  
            errors['username_error'] = "username already taken"
            return template("signup", errors)

        session_id = sessions.begin_session(username)
        print "session id: ", session_id
        response.set_cookie("session", session_id)
        redirect("/")
    else:
        print "user did not validate"
        return template("signup", errors)


####
# PUTS
####

@put('/edithabit')
def edit_habit():
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories')

    habits.update(name, times, occurence, reminders, categories)

    redirect('/')

####
# STATIC FILES
####

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/')

####
# ERRORS
####

@error(404)
def error404(error):
    return template('404')

####
# HELPER FUNCTIONS
####

def check_logged_in():
    cookie = request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        redirect("/signin")
    else:
        return username



client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)
sessions = Session.Session(database)
users = User.User(database)

debug(True)
run(host='localhost', port=8080) 