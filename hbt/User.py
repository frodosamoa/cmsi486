import hashlib
import pymongo

class User:

    def __init__(self, connection):
        self.connection = pymongo.MongoClient('localhost', 27017)
        self.users = self.connection.hbt.users
        self.SECRET = 'wow such secret'

    def create_password_hash(self, password):
        return hashlib.sha256(password).hexdigest()

    def add_user(self, username, password):
        password_hash = self.create_password_hash(password)

        user = {'_id': username, 'password': password_hash}

        try:
            self.users.insert(user, safe=True)
        except pymongo.errors.OperationFailure:
            print "we have a mongo error"
            return False
        except pymongo.errors.DuplicateKeyError as e:
            print "that username is already taken"
            return False

        return True