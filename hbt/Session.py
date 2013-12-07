import sys
import random
import string
import pymongo

class Session:

    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.sessions = self.connection.hbt.sessions

    def random_string(self, num_chars=32, chars=string.ascii_letters):
        return ''.join(random.choice(chars) for x in range(num_chars))

    def begin_session(self, username):

        session_id = self.random_string()
        session = {'username': username, '_id': session_id}

        try:
            self.sessions.insert(session, safe=True)
            print "inserting the session"
        except:
            print "unexpected error:", sys.exc_info()[0]
            return None

        return str(session['_id'])

    def end_session(self, session_id):

        if session_id is None:
            return

        self.sessions.remove({'_id': session_id})

        return