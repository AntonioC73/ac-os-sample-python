from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello AC-v2-World!"

if __name__ == "__main__":
    application.run()
