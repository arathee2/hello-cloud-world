from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    msg = """This is a simple flask app that is continuously being deployed using 
    Google Cloud Platform (GCP). Append '/time' after the base URL (after .com) to 
    see today's date and time.
    """
    return msg

@app.route('/time')
def time():
    msg = f"Current date and time is: {datetime.datetime.now()}"
    return msg

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)