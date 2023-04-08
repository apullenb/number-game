from flask import Flask, render_template, session

app = Flask(__name__)




@app.route("/", methods=['GET'])
def success():
        return '<h1>Welcome!</>'
    



if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5000)