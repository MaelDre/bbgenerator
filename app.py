import os
from flask import Flask
from BBGen import bbgenerator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body>'
    page += '<h1>Voici une idée de génie, ou pas.</h1>'
    page += '<h2>'
    page += bbgenerator.generate_buzz()
    page += '</h2></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
