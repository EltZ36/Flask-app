from project import app, bcrypt, login_manager
from project.models import Student
from project.forms import LoginForm
from flask import render_template, url_for, request, redirect, flash
from flask_login import current_user, login_required, login_user, logout_user

# Load user or return None if not found
@login_manager.user_loader
def load_user(id):

    # Query for User
    user = Student.query.get(int(id))
    # If user not found return None else return User object
    if user is None:
        return None

    return user


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

@app.route('/list')
@login_required
def listThings():
  names = ['Elon Musk', 'Bill Gates', 'Mark Zuckerberg']
  return render_template('names.html', names=names)

@app.route('/login', methods=['GET', 'POST'])
def login():

    # If user is logged in stop them from logging in again
    if current_user.is_authenticated:
        flash('You are already logged in', 'warning')
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():

        # Get input email
        firstname = form.firstname.data.lower()

        # Query for user by email
        user = Student.query.filter_by(firstname=firstname).first()

        # User not found
        if user is None:
            flash(
                'Login Unsuccessful. User dosen\'t exsist',
                'error')
        else:

            # Check user password
            if bcrypt.check_password_hash(user.password, form.password.data):

                # Login user
                login_user(user, remember=form.remember.data)

                # Get next page
                next_page = request.args.get('next')

                # Redirect to index or to next
                flash('Logged in successfully.', 'success')
                return redirect(next_page) if next_page else redirect(
                    url_for('index'))

            # Password is incorrect
            else:
                flash(
                    'Login Unsuccessful. Please check email and password',
                    'error')

    # Return login form
    return render_template('login.html', form=form)
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    # If user is logged in stop them from logging in again
    if current_user.is_authenticated:
        flash('You are already logged in', 'warning')
        return redirect(url_for('home'))

    form = SignUpForm()

    if form.validate_on_submit():

        # Get input email
        email = form.email.data.lower()
        name = form.name.data.lower()
        password = bcrypt.generate_password_hash(form.password.data)

        print(email, name, password)

        # Query for user by email
        # user = Student.query.filter_by(firstname=firstname).first()
        user = MongoStudent.query({'email': email})

        # User not found
        if user is not None:
            flash(
                'Sign Up Unsuccessful. User already exsists',
                'error')
            print('login unsuccessful user already exists')
        else:

            # let's create the user
            new_user = MongoStudent(email, name, password)

            # add user to the database
            new_user.insert_user()

            # Redirect to index or to next
            flash('Sign up successfully.', 'success')
            return redirect(url_for('home'))

    # Return login form
    return render_template('signup.html', form=form)

import requests

query = 'the lord of the rings'

def get_amazon_book_id(params):
    openlib_API_url = 'http://openlibrary.org/search.json'

    res = requests.get(url=openlib_API_url, params=params)

    data = res.json()

    # print(ata['docs'][0]['id_amazon'])

    return data['docs'][0]['id_amazon']

@app.route('/getbooks', methods=['GET', 'POST'])
def getbooks():

    book_form = BookForm()

    if book_form.validate_on_submit():
        book_name = book_form.book.data.lower()
        params = {'q': book_name}
        data = get_amazon_book_id(params)

        return str(data)

    return render_template('bookform.html', form=book_form)
