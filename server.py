from flask import Flask, render_template, redirect, session 
app = Flask(__name__)   
app.secret_key = '1472417647'

@app.route('/')
def count():
    if "counter" not in session: 
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def resetCount():
    session.pop('counter')		
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)