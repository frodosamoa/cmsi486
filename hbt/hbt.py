import json
import Habit
import Day
import Session
import User
import cgi
import re

from bottle import route, get, post, put, debug, run, request, redirect, template, static_file, error, response
from pymongo import MongoClient


####
# ROUTES
####

@route('/signup')
def get_signup():
    return template('signup', dict(username='', password='', password_error='', username_error='', verify_error =''))

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
    return template('new_habit', dict(username=username, name='', times = '', occurence='', reminders='', categories=''))

@route('/categories')
def get_categories():
    username = check_logged_in()
    return template('categories', dict(username=username));

@route('/graphs')
def get_graphs():
    username = check_logged_in()
    return template('graphs', dict(username=username));

####
# POSTS
####

@post('/newhabit')
def post_new_habit():
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories').split(',')
    habits.insert_habit(username, name, times, occurence, reminders, categories)

    redirect('/')

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

# helper function to see if we are logged in
def check_logged_in():
    cookie = request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        redirect("/signup")
    else:
        return username


client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)
sessions = Session.Session(database)
users = User.User(database)

debug(True)
run(host='localhost', port=8080) 