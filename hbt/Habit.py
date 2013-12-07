import sys
import re
import pymongo

class Habit:
   
    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.habits = self.connection.hbt.habits


    def insert_habit(self, username, name, times, occurence, reminders, categories):
        print 'inserting habit', username, name, times, occurence, reminders, categories

        habit = {'username' : username,
                 'name': name,
                 'interval' : {
                        'times' : times,
                        'occurence' : occurence
                    },
                 'reminders' : reminders,
                 'categories' : categories
                }
        try:
            self.habits.insert(habit, safe=True)
            print 'inserting the habit'
        except pymongo.errors.OperationFailure:
            print "we have a mongo error"
            return False
        except:
            print 'error inserting habit'
            print 'unexpected error:', sys.exc_info()[0]

   
    def get_habits(self, username):

        cursor = self.habits.find({'username' : username})

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

    def update_habit(self):
        return 0

    def get_habit_by_category(self, username, category):

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








