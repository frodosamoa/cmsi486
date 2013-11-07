import json
import bottle
import pymongo
import Habit
import cgi
import re

from pymongo import MongoClient

@bottle.route('/')
def get_habits():
    l = habits.get_habits(10)
    return bottle.template('habits_template', dict(myhabits=l))

# @bottle.get('/post/<permalink>')
# def habit(permalink='notfound'):

#     print 'about to query on permalink = ', permalink
#     post = posts.get_post_by_permalink(permalink)

#     if post is None:
#         bottle.redirect('/post_not_found')

#     # init comment form fields for additional comment
#     comment = {'name': '', 'body': '', 'email': ''}

#     return bottle.template('entry_template', dict(post=post, username=username, errors='', comment=comment))


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


client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)

bottle.debug(True)
bottle.run(host='localhost', port=8080) 