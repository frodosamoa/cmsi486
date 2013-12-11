import sys
import re
import pymongo
import datetime

class Habit:
   
    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.habits = self.connection.hbt.habits


    def insert_habit(self, username, name, interval, occurence, reminders, categories):
        print 'inserting habit', username, name, interval, occurence, reminders, categories

        today = datetime.datetime.now().date()

        habit = { 'username'           : username,
                  '_id'                : name,
                  'interval'           : interval,
                  'occurence'          : occurence,
                  'reminders'          : reminders,
                  'categories'         : categories,
                  'dateCreated'        : str(today), 
                  'completedIntervals' : {
                        '0': False
                  }
                }
        try:
            self.habits.insert(habit, safe=True)
            print 'inserting the habit'
        except:
            print 'error inserting habit'
            print 'unexpected error:', sys.exc_info()[0]

   
    def get_user_habits(self, username):

        cursor = self.habits.find({'username' : username})

        l = []

        for habit in cursor:
            l.append({'name' : habit['_id'],
                      'interval' : habit['interval'],
                      'occurence' : habit['occurence'],
                      'reminders' : habit['reminders'],
                      'categories' : habit['categories'],
                      'dateCreated' : habit['dateCreated'],
                      'completedIntervals' : habit['completedIntervals']})

        return l

    def get_habit(self, name):
        cursor = self.habits.find({'_id': name})

        habit = {'name': cursor[0]['_id'],
                  'interval' : cursor[0]['interval'],
                  'occurence' : cursor[0]['occurence'],
                  'reminders' : cursor[0]['reminders'],
                  'categories' : cursor[0]['categories'],
                  'dateCreated' : cursor[0]['dateCreated'],
                  'completedIntervals' : habit['completedIntervals']}

        return habit

    def update_habit_intervals(self, habit):
        self.habits.update({'_id' : habit['name']}, {'$set': {'completedIntervals' : habit['completedIntervals']} }, upsert=False)

    def refresh_habits(self, username):
        habits = self.get_user_habits(username)
        today = datetime.datetime.now().date()
        
        for habit in habits:
            time_delta = today - datetime.datetime.strptime(habit['dateCreated'], "%Y-%m-%d").date()
            print habit['completedIntervals']
            print time_delta.days
            for day in range(time_delta.days):
                if str(day) not in habit['completedIntervals']:
                    habit['completedIntervals'][str(day)] = False
            self.update_habit_intervals(habit)

    def get_oldest_habit_date(self, username):
        cursor = self.habits.find({'username' : username}).sort('dateCreated', pymongo.ASCENDING).limit(1)

        return cursor[0]['dateCreated']

    def get_habits_by_category(self, username, category):

        cursor = self.habits.find({'username' : username}, {'categories' : { '$in' : [category] } } )

        l = []

        for habit in cursor:
            l.append({'name': habit['_id'],
                      'interval' : habit['interval'],
                      'occurence' : habit['occurence'],
                      'reminders' : habit['reminders'],
                      'categories' : habit['categories']})

        return l