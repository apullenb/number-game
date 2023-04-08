import random
from flask import Flask, render_template, session

app = Flask(__name__)




@app.route("/", methods=['GET'])
def success():
        return '<h1>Welcome!</>'
    
@app.route('/game', methods=['GET'])
def start_game():
    numbers = []
    for n in range(1, 100): 
            numbers.append(n)
    number = random.choice(numbers)
    return render_template('index.html', number=number)


if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5000)