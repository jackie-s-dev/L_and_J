from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html", example_var="HEWWO BITCH")

if __name__ == "__main__":
    app.run()