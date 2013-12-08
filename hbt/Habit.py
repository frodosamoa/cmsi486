import sys
import re
import pymongo
import datetime

class Habit:
   
    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.habits = self.connection.hbt.habits


    def insert_habit(self, username, name, times, occurence, reminders, categories):
        print 'inserting habit', username, name, times, occurence, reminders, categories

        today = datetime.datetime.now().date()

        habit = {'username' : username,
                 'name': name,
                 'interval' : {
                        'times' : times,
                        'occurence' : occurence
                    },
                 'reminders' : reminders,
                 'categories' : categories,
                 'dateCreated' : str(today)
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
            l.append({'name': habit['name'],
                      'interval' : {
                          'times' : habit['interval']['times'],
                          'occurence' : habit['interval']['occurence']
                        },
                      'reminders' : habit['reminders'],
                      'categories' : habit['categories'],
                      'dateCreated' : habit['dateCreated']})

        return l

    def update_habit(self):
        return 0

    def get_oldest_habit_date(self, username):
        cursor = self.habits.find({'username' : username}).sort('dateCreated', pymongo.ASCENDING).limit(1)

        return cursor[0]['dateCreated']

    def get_habits_by_category(self, username, category):

        cursor = self.habits.find({'username' : username}, {'categories' : { '$in' : [category] } } )

        l = []

        for habit in cursor:
            l.append({'name': habit['name'],
                      'interval' : {
                          'times' : habit['interval']['times'],
                          'occurence' : habit['interval']['occurence']
                        },
                      'reminders' : habit['reminders'],
                      'categories' : habit['categories']})

        return l