from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'meddlingKids'

@app.route('/', methods=['GET', 'POST'])
def index_counter():
    session['count'] += 0
    if request.method == 'POST':
        if request.form['update'] == 'plus_one':
            session['count'] += 1 
            # return redirect ('index.html', count=session['count'])
        elif request.form['update'] == 'plus_two':
            session['count'] += 2
            # return redirect ('index.html', count=session['count'])
        elif request.form['update'] == 'reset':
            session['count'] = 0
            # return redirect ('index.html', count=session['count'])
        else:
            pass  
    elif request.method == 'GET':
        return render_template ('index.html', count = session['count'])

app.run(debug=True)