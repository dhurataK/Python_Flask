from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def get_counter():
    try:
        session['counter']
    except:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route('/ninja', methods=['POST'])
def increment():
    session['counter']+=1
    return redirect('/')

@app.route('/hacker', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')
# def buttonClicked():
#     if request.method == 'POST':
#          if request.form['button'] == '+2':
#             session['counter'] +=1
#          elif request.form['button'] == 'Reset':
#             session['counter'] = 0
app.run(debug=True)
