import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret123'




@app.route("/", methods=['GET'])
def success():
    number = random.randint(1,100)
    session['number'] = number
    session['chances'] = 5
    return render_template('index.html')
    
@app.route('/game', methods=['GET','POST'])
def start_game():
    if not request.form:
        guess = ''
        return render_template('game.html', number=session['number'], guess=guess, chances=session['chances'])
    if not request.form['guessed'].isdigit():
        guess = 'Not a Number'
        return render_template('game.html', number=session['number'], guess=guess, chances=session['chances'])
    else:
        guess = int(request.form['guessed'])
        session['chances'] -= 1
        return render_template('game.html', number=session['number'], guess=guess, chances=session['chances'])
    
@app.route('/destroy_session')
def reset_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5000)