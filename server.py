import random
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'secret123'




@app.route("/", methods=['GET'])
def success():
    number = random.randint(1,100)
    session['number'] = number
    return render_template('index.html')
    
@app.route('/game', methods=['GET'])
def start_game():
    return render_template('game.html', number=session['number'])
    

   


if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5000)