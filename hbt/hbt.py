import json
import bottle
import pymongo
import Habit
import cgi
import re

from bottle import route, get, post, put, debug, run, request, redirect, template
from pymongo import MongoClient

@route('/')
def get_habits():
    l = habits.get_habits(10)
    return template('habits_template', dict(myhabits=l))


@route('/login')
def login():
    return template('login')

@get('/newhabit')
def newhabit():

    return template('newhabit_template', dict(name='', times = '', occurence='', reminders=''))

@post('/newhabit')
def post_new_habit():
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories')
    habits.insert_habit(name, times, occurence, reminders, categories)

    redirect('/')

@put('/edithabit')
def edit_habit():
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories')

    habits.insert_habit(name, times, occurence, reminders, categories)

    redirect('/')


client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)
# checks = Checks.Check(database)

debug(True)
run(host='localhost', port=8080) 