import sys
import re
import pymongo

class Habit:
   
    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.habits = self.connection.hbt.habits

   
    def insert_habit(self, name):
        print "inserting habit", name

        habit = {"name": name}
        try:
            self.habits.insert(habit)
            print "inserting the habit"
        except:
            print "error inserting habit"
            print "unexpected error:", sys.exc_info()[0]

   
    def get_habits(self, num_habits):

        cursor = self.habits.find().limit(num_habits)

        l = []

        for habit in cursor:
            l.append({'name': habit['name']})

        return l










