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

        session = {'username': username, '_id': self.random_string()}

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

    def get_session(self, session_id):

        if session_id is None:
            return None

        return self.sessions.find_one({'_id': session_id})

    def get_username(self, session_id):

        session = self.get_session(session_id)

        if session is None:
            return None
        else:
            return session['username']