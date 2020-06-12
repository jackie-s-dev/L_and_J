from flask import *
from dictator_api import get_dictators

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html", example_var="HEWWO BITCH")

@app.route('/jackies_api', methods=['POST', 'GET'])
def jackies_api():
    """
    This is a test page for the API
    """
    if request.method == 'POST':
        search_query = request.form['search_dictator']
        names, ext_links = get_dictators(search_query, 10)
        return render_template("jackies_api.html", names=names, ext_links=ext_links)
    return render_template("jackies_api.html")

if __name__ == "__main__":
    app.run()
