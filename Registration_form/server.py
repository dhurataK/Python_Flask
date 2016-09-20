from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_NINJA= re.compile(r'.*?[A-Z]+.*?[0-9]+|.*?[0-9]+.*?[A-Z]')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    name = request.form['first_name']
    last = request.form['last_name']
    birthday = request.form['birthday']
    email = request.form['email']
    password = request.form['password']
    confirm_passowrd = request.form['confirm_passowrd']
    date = datetime.datetime.strptime

    #validating first_name and last_name
    if len(name) < 1:
        flash("First Name cannot be blank!")
    elif not str.isalpha(str(name)):
        flash("First Name cannot contain numbers!")
    if len(last) < 1:
        flash("Last Name cannot be blank!")
    elif not str.isalpha(str(last)):
        flash("Last Name cannot contain numbers!")

    #validating birthday
    if len(birthday) < 1:
        flash("Birthday cannot be blank!")
    elif not date(birthday,"%m/%d/%Y"):
        flash("Not a valid birthday!")
    elif date(birthday,"%m/%d/%Y") >= datetime.datetime.today():
        flash("You're not born yet!")

    #validating email
    if len(email) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")

    #validating password
    if len(password) < 1:
        flash("Password cannot be blank!")
    elif not len(password) >= 8:
        flash("Password must be longer than 8 characters!")
    elif not PASSWORD_NINJA.match(password):
        flash("Password must contain an Upper letter and a Number!")

    #validating confirm_passowrd
    if len(confirm_passowrd) < 1:
        flash("Confirm Password cannot be blank!")
    elif not sorted(list(str(confirm_passowrd))) == sorted(list(str(password))):
        flash("Passwords must be the same!")
    #Everything went good submit the information
    else:
        flash("Thanks for submitting your information!")
    return redirect('/')
app.run(debug=True)
