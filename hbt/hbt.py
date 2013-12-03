import json
import Habit
import Day
import Session

from bottle import route, get, post, put, debug, run, request, redirect, template, static_file, error 
# get_url
from pymongo import MongoClient



@route('/signin')
def signin():
    return template('signin')

@route('/signup')
def signup():
    return template('signup')



@route('/')
def get_habits():
    l = habits.get_habits(10)
    return template('habits', dict(myhabits=l))


@route('/newhabit')
def newhabit():
    return template('new_habit', dict(name='', times = '', occurence='', reminders='', categories=''))

@post('/newhabit')
def post_new_habit():
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories').split(',')
    habits.insert_habit(name, times, occurence, reminders, categories)

    redirect('/')




@route('/categories')
def get_categories():
    return template('categories');

@route('/graphs')
def get_graphs():
    return template('graphs');




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


client = MongoClient('localhost', 27017)
database = client.hbt
habits = Habit.Habit(database)
sessions = Session.Session(database)

debug(True)
run(host='localhost', port=8080) 