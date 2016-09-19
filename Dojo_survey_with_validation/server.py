from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "verySecret!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def validate():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(name) == 0 and len(comment) == 0:
        flash("Name shouldn't be blank!")
        flash("Comment field shouldn't be blank!")
        return redirect('/')
    elif len(name) > 0 and len(comment) == 0:
        flash("Comment field shouldn't be blank!")
        return redirect('/')
    elif len(name) == 0 and len(comment) > 0:
        flash("Name shouldn't be blank!")
        return redirect('/')
    elif len(comment) > 120:
        flash("Comments shouldn't exceed 120 characters!")
        return redirect('/')
    else:
        return render_template('result.html', name= name, location= location, language = language, comment = comment)

app.run(debug=True)
