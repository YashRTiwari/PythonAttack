from flask import Flask

#Create an object to store flask app instance
app = Flask(__name__)


# URL where you'll view your website
# @app.route('/') --> Decorator
@app.route('/')
def home():
    return "Home Page"


@app.route('/about/')
def about():
    return "About Page"

if __name__ == "__main__":
    app.run(debug= True)

# When you import this main.py script somewhere then __name__ = "main.py"
# whereas if you execute this file then python assigns __name__ = "__main__"