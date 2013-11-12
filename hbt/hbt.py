import json
import bottle
import pymongo
import Habit
import cgi
import re

from bottle import static_file
from pymongo import MongoClient

@bottle.route('/')
def get_habits():
    l = habits.get_habits(10)
    return bottle.template('habits_template', dict(myhabits=l))

# @bottle.get('/categories')
# def get_categories():


@bottle.get('/newhabit')
def get_newhabit():

    return bottle.template('newhabit_template', dict(name='', times = '', occurence='', reminders=''))

@bottle.post('/newhabit')
def post_newhabit():
    name = bottle.request.forms.get('name')
    times = bottle.request.forms.get('times')
    occurence = bottle.request.forms.get('occurence')
    reminders = bottle.request.forms.get('reminders')

    habits.insert_habit(name, times, occurence, reminders)

    bottle.redirect('/')


@bottle.get('/<filename:re:.*\.js>')
def bootstrap_javascript(filename):
    return static_file(filename, root='bootstrap/js')

@bottle.get('/<filename:re:.*\.css>')
def bootstrap_stylesheet(filename):
    return static_file(filename, root='bootstrap/css')

@bottle.get('/<filename:re:.*\.png>')
def bootstrap_images(filename):
    return static_file(filename, root='bootstrap/img')

client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)

bottle.debug(True)
bottle.run(host='localhost', port=8080) 