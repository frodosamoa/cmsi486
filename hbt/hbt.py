import json
import Habit
import Day
import cgi
import re

from bottle import Bottle, route, get, post, put, debug, run, request, redirect, template, static_file 
# get_url
from pymongo import MongoClient

@route('/')
def get_habits():
    l = habits.get_habits(10)
    # return template('habits_template', dict(myhabits=l), get_url=get_url)
    return template('habits', dict(myhabits=l))


@route('/login')
def login():
    return template('login')

@route('/newhabit')
def newhabit():
    return template('new_habit', dict(name='', times = '', occurence='', reminders='', categories=''))

@post('/newhabit')
def post_new_habit():
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories')
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


client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)
days = Day.Day(database)

debug(True)
run(host='localhost', port=8080) 