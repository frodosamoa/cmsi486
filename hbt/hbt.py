import json
import Habit
import Day
import Session
import User
import cgi
import datetime
import hashlib

from bottle import route, get, post, put, debug, run, request, redirect
from bottle import template, static_file, error, response
from pymongo import MongoClient


####
# ROUTES
####

@route('/signup')
def get_signup():
    return template('signup', dict(username='', password='', password_error='',
                                   username_error='', verify_error =''))

@route('/signin')
def get_signin():
    return template('signin', dict(username='', password='', login_error=''))

@route('/')
@route('/habits')
def get_habits():
    username = check_logged_in()
    user = users.get_user(username)
    today = datetime.datetime.now().date()
    earliest_date, delta = None, None

    l = habits.get_user_habits(username)
    if len(l) > 0:
        earliest_date = habits.get_oldest_habit_date(username)
        earliest_date = datetime.datetime.strptime(earliest_date, '%Y-%m-%d').date()
        delta = today - earliest_date

    habits.refresh_habits(username)


    return template('habits', dict(title='habits', user=user, myhabits=l, 
                                   max_days=delta.days + 1 if delta else -1, datetime=datetime))

@route('/habit/<name>')
def habit():
    habit = habit.get_habit(name)
    return template('habit', dict(habit=habit, name=habit['_id']))

@route('/newhabit')
def newhabit():
    username = check_logged_in()
    return template('new_habit', dict(username=username, name='', interval = '',
                                      occurence='', reminders='', categories=''))

@route('/categories')
def get_categories():
    username = check_logged_in()
    categories = habits.get_categories(username)
    return template('categories', dict(title='categories', username=username,
                                       categories=categories))

@route('/profile')
def get_profile():
    username = check_logged_in()
    user = users.get_user(username)
    l = habits.get_user_habits(username)
    categories = habits.get_categories(username)
    best_habits = habits.get_best_habits(username)
    worst_habits = habits.get_worst_habits(username)
    return template('profile', dict(title='profile', user=user, habits=l,
                                    categories=categories, best_habits=best_habits,
                                    worst_habits=worst_habits))

@route('/graphs')
def get_graphs():
    username = check_logged_in()
    return template('graphs', dict(title='graphs', username=username))

@route('/logout')
def logout():
    cookie = request.get_cookie('session')
    sessions.end_session(cookie)
    response.set_cookie('session', '')
    redirect('/signin')

####
# POSTS
####

@post('/newhabit')
def post_new_habit():
    username = check_logged_in()
    name = request.forms.get('name')
    interval = request.forms.get('interval')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories').split(',')
    habits.insert_habit(username, name, interval, occurence, reminders, categories)

    redirect('/')

@post('/')
def update_all_habit_intervals():
    username = check_logged_in()
    habit_list = habits.get_user_habits(username)
    today = datetime.datetime.now().date()

    for habit in habit_list:
        date_created = datetime.datetime.strptime(habit['dateCreated'], '%Y-%m-%d').date()
        days_active = today - date_created
        for day in range(days_active.days, -1, -1):
            habit_instance = str(habit['name'].replace(' ', '-').replace('\'', '') + '-' + str(today - datetime.timedelta(days=day)))
            print habit_instance, request.forms.get(habit_instance)
            habit['completedIntervals'][str(day)] = request.forms.get(habit_instance) == 'true'
        habits.update_habit_intervals(habit)

    redirect('/')

@post('/signin')
def signin():
    username = request.forms.get('username')
    password = request.forms.get('password')

    print 'user submitted ', username, 'pass ', password

    user_record = users.validate_login(username, password)
    if user_record:
        session_id = sessions.begin_session(user_record['_id'])

        if session_id is None:
            redirect('/internal_error')

        cookie = session_id
        response.set_cookie('session', cookie)

        habits.refresh_habits(username)

        redirect('/')

    else:
        return template('signin', dict(username=cgi.escape(username), password='',
                                    login_error='invalid login'))

@post('/signup')
def signup():
    username = request.forms.get('username')
    password = request.forms.get('password')
    verify = request.forms.get('verify')

    errors = {'username': cgi.escape(username)}
    if users.validate_signup(username, password, verify, errors):

        if not users.add_user(username, password):  
            errors['username_error'] = 'username already taken'
            return template('signup', errors)

        session_id = sessions.begin_session(username)
        print 'session id: ', session_id
        response.set_cookie('session', session_id)
        redirect('/')
    else:
        print 'user did not validate'
        return template('signup', errors)

####
# PUTS
####

## TODO

@put('/edithabit')
def edit_habit():
    name = request.forms.get('name')
    times = request.forms.get('times')
    occurence = request.forms.get('occurence')
    reminders = request.forms.get('reminders')
    categories = request.forms.get('categories')

    habits.update(name, times, occurence, reminders, categories)

    redirect('/')

####
# STATIC FILES
####

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/')

####
# ERRORS
####

@error(404)
def error404(error):
    cookie = request.get_cookie('session')
    username = sessions.get_username(cookie)
    return template('404', dict(username=username))

####
# HELPER FUNCTIONS
####

def check_logged_in():
    cookie = request.get_cookie('session')
    username = sessions.get_username(cookie)
    if username is None:
        redirect('/signin')
    else:
        return username

client = MongoClient('localhost', 27017)
database = client.hbt

habits = Habit.Habit(database)
sessions = Session.Session(database)
users = User.User(database)

debug(True)
run(host='localhost', port=8080) 