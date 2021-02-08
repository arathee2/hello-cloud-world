from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    msg = """This is a simple flask app that is continuously being deployed using 
    Google Cloud Platform (GCP). Append '/time' after the base URL (after .com) to 
    see the date and time when this page was last updated.
    """
    return msg

@app.route('/time')
def time():
    msg = f"Website last updated on: {datetime.datetime.now()}"
    return msg

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)