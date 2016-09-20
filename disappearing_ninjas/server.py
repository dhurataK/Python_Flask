from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    ninja = 'all'
    return render_template('ninja.html', ninja = ninja)

@app.route('/ninja/<ninja_color>')
def dojos(ninja_color):
    return render_template('ninja.html', ninja = ninja_color)

app.run(debug=True)
