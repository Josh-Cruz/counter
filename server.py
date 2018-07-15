from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'meddlingKids'

@app.route('/', methods=['GET', 'POST'])
def index_counter():
    if 'count' not in session:
        session['count'] = 1
    if request.method == 'POST':
        if request.form['update'] == 'plus_one':
            session['count'] += 1 
            print session['count']
        elif request.form['update'] == 'plus_two':
            session['count'] += 2
            print session['count']
        elif request.form['update'] == 'reset':
            session['count'] = 0
            print session['count']
        return render_template('index.html', count=session['count'])
    elif request.method == 'GET':
        return render_template ('index.html', count = session['count'])





app.run(debug=True)
