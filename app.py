from flask import *
from dictator_api import get_search, Quiz

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
        names, ext_links = get_search(search_query, 10)
        return render_template("jackies_api.html", names=names, ext_links=ext_links)
    return render_template("jackies_api.html")

@app.route('/quiz_example', methods=['POST', 'GET'])
def quiz_example():
    """
    Example quiz page, using the API
    """
    # this is pointlessly bulky
    if request.method =="POST":
        # answer a quiz
        regime_quiz = Quiz("https://en.wikipedia.org/wiki/List_of_totalitarian_regimes")

        answers = [request.form['foods'], request.form['word_vibe'],
                   request.form['socks_indoors'], request.form['universe'],
                   request.form['worms']]

        # you do not need to parse radio button inputs
        result = regime_quiz.p_randomize(answers)
        return render_template("quiz_example.html", completed=True, result=result[0], vals=result[1])

    return render_template("quiz_example.html")

if __name__ == "__main__":
    app.run()
