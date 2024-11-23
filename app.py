from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/must_visit')
def must_visit():
    return render_template('must_visit.html')

@app.route('/dining')
def dining():
    return render_template('dining.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
