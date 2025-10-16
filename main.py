from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html', scroll_to='about')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/programming')
def programming():
    return render_template('programming.html')

@app.route('/home')
def back_button_programming():
    return render_template('index.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

# @app.route('/home')
# def back_button_travel():
#     return render_template('index.html')

@app.route('/nature')
def nature():
    return render_template('nature_blog.html')

# @app.route('/home')
# def back_button_nature():
#     return render_template('index.html')


app.run(debug=True)
