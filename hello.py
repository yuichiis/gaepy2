import flask, jinja2
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World! flask:%s, jinja2:%s' % (flask.__version__, jinja2.__version__)

if __name__ == "__main__":
    app.run()
