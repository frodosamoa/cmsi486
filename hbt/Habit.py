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
                        '0': False,
                        'count' : 0
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
        habit = self.habits.find_one({'_id': name})

        habit = {'name': habit['_id'],
                  'interval' : habit['interval'],
                  'occurence' : habit['occurence'],
                  'reminders' : habit['reminders'],
                  'categories' : habit['categories'],
                  'dateCreated' : habit['dateCreated'],
                  'completedIntervals' : habit['completedIntervals']}

        return habit


    def update_habit_interval_count(self, habit, count):
        self.habits.update({'_id' : habit['name']}, {'$set': {'completedIntervals.count' : count} }, upsert=False)

    def update_habit_intervals(self, habit):
        self.habits.update({'_id' : habit['name']}, {'$set': {'completedIntervals' : habit['completedIntervals']} }, upsert=False)

    def refresh_habits(self, username):
        habits = self.get_user_habits(username)
        today = datetime.datetime.now().date()
        count = 0
        
        for habit in habits:
            time_delta = today - datetime.datetime.strptime(habit['dateCreated'], "%Y-%m-%d").date()
            for day in range(time_delta.days + 1):
                if str(day) not in habit['completedIntervals']:
                    habit['completedIntervals'][str(day)] = False
                else:
                    count = count + 1 if habit['completedIntervals'][str(day)] else count

            self.update_habit_intervals(habit)
            self.update_habit_interval_count(habit, count)
            count = 0

        

    def get_oldest_habit_date(self, username):
        cursor = self.habits.find({'username' : username}).sort('dateCreated', pymongo.ASCENDING).limit(1)

        return cursor[0]['dateCreated']

    def get_categories(self, username):
        l = self.get_user_habits(username)
        category_set = set()
        for habit in l:
            for cat in habit['categories']:
                category_set.add(cat)

        return category_set

    def get_best_habits(self, username):
        cursor = self.habits.find({'username' : username}).sort('completedIntervals.count', pymongo.ASCENDING).limit(10)
        l = []
        for habit in cursor:
            l.append(habit['_id'])

        return l

    def get_worst_habits(self, username):
        cursor = self.habits.find({'username' : username}).sort('completedIntervals.count', pymongo.DESCENDING).limit(10)
        l = []
        for habit in cursor:
            l.append(habit['_id'])

        return l


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