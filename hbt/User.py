import random
import string
import hashlib
import pymongo
import re

class User:

    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.users = self.connection.hbt.users
        self.SECRET = 'wow such secret'

    def salt(self, num_chars=12, chars=string.ascii_letters):
        return ''.join(random.choice(chars) for x in range(num_chars))

    def create_password_hash(self, password, salt=None):
        if salt == None:
            salt = self.salt()

        return hashlib.sha256(password + salt).hexdigest() + "," + salt

    def add_user(self, username, password):
        password_hash = self.create_password_hash(password)

        user = {'_id': username, 'password': password_hash}

        try:
            self.users.insert(user, safe=True)
            print "inserting the user"
        except pymongo.errors.OperationFailure:
            print "we have a mongo error"
            return False
        except pymongo.errors.DuplicateKeyError as e:
            print "that username is already taken"
            return False

        return True

    def validate_login(self, username, password):

        user = None
        try:
            user = self.users.find_one({'_id': username})
        except:
            print "couldn't find that user"

        if user is None:
            print "user isn't in database"
            return None

        salt = user['password'].split(',')[1]

        if user['password'] != self.create_password_hash(password, salt):
            print "password doesn't match"
            return None

        return user

    def validate_signup(self, username, password, verify, errors):
        USER_REGEX = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

        errors['username_error'] = ""

        if not USER_REGEX.match(username):
            errors['username_error'] = "username must be composed of letters and numbers"
            return False

        return True