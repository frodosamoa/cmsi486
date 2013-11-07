import json
import bottle
import pymongo
import Habit
import cgi
import re

from pymongo import MongoClient

@bottle.route('/')
def habits():
    l = habits.get_habits(10)
    return bottle.template('habits_template', dict(myhabits=l))




client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)

bottle.debug(True)
bottle.run(host='localhost', port=8080) 