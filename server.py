from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template("counter.html")


@app.route('/count')
def count():
    if 'count' in session:
        session['count'] += 1
    return redirect('/')

@app.route('/increment_2')
def counter():
    session['count'] += 2
    return redirect ('/')

@app.route('/destroy_session')
def rootRouteDestroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(port = 8000, debug=True)
