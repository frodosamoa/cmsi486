import sys
import re
import pymongo

class Day:
   
    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.habits = self.connection.hbt.days

   
    def insert_day(self, date, completed_habits):
        print 'inserting day', date, completed_habits

        day = {'date': date,
                'completed_habits' : completed_habits
              }
        try:
            self.habits.insert(day)
            print 'inserting the day'
        except:
            print 'error inserting day'
            print 'unexpected error:', sys.exc_info()[0]

   
    def get_days(self, num_days):

        cursor = self.habits.find().limit(num_days)

        l = []

        for day in cursor:
            l.append({'date': day['date'],
                      'completed_habits' : day['completed_habits']})

        return l

    def update_day(self, day):








