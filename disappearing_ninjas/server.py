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
    ninjas = {'blue':'leonardo','orange':'michelangelo','red':'raphael', 'purple':'donatello'}
    if ninja_color in ninjas:
        ninja = ninjas[ninja_color]
    else:
        ninja = 'notapril'
    return render_template('ninja.html', ninja = ninja)

app.run(debug=True)
