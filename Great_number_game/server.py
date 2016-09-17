from flask import Flask, render_template, request, redirect, session, flash
import random
app= Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guessedValue = int(request.form['enteredValue'])
    session['number'] = 50 #testing
    # session['number'] = random.randrange(0, 101)
    print guessedValue,"randrom "+ str(session['number'])
    if guessedValue < session['number']:
        flash("Too low!")
        session['color'] = 'red'
    elif guessedValue > session['number']:
        flash("Too High!")
        session['color'] = 'red'
    else:
        flash(str(guessedValue)+" was the number!")
        session['color'] = 'green'
    return redirect('/')

@app.route('/reset')
def reset():
    session['number'] = random.randrange(0, 101)
    return redirect('/')

app.run(debug=True)
