import random
import string
import hashlib
import pymongo
import re
import datetime

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

        today = datetime.datetime.now().date()

        user = {'_id': username,
                'password': password_hash,
                'dateJoined': str(today)}

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

    def get_user(self, username):

        cursor = self.find_user(username)
        user = {'username': cursor['_id'], 'dateJoined' : cursor['dateJoined']}

        return user


    def validate_login(self, username, password):

        user = self.find_user(username)

        salt = user['password'].split(',')[1]

        if user['password'] != self.create_password_hash(password, salt):
            print "password doesn't match"
            return None

        return user

    def find_user(self, username):

        user = None
        try:
            user = self.users.find_one({'_id': username})
        except:
            print "couldn't find that user"

        if user is None:
            print "user isn't in database"
            return None

        return user

    def validate_signup(self, username, password, verify, errors):
        USER_REGEX = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        PASSWORD_REGEX = re.compile(r"^.{6,30}$")

        errors['username_error'] = ""
        errors['password_error'] = ""
        errors['verify_error'] = ""

        if not USER_REGEX.match(username):
            errors['username_error'] = "username must be composed of letters and numbers"
            return False

        if not PASSWORD_REGEX.match(password):
            if (len(password) < 6 or len(password) > 40):
                errors['password_error'] = "password must be between 6 and 30 characters long"
            else:
                errors['password_error'] = "invalid password"
            return False

        if password != verify:
            errors['verify_error'] = "passwords don't match"
            return False

        return True