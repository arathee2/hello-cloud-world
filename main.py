from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    msg = """This is a simple flask app continuously being deployed using 
    Google Cloud Platform. Append '/time' to the current URL to see today's
    date and time.
    """
    return msg

@app.route('/time')
def time():
    return print(datetime.datetime.now())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)