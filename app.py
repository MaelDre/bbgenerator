import os
from flask import Flask
from BBGen import bbgenerator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body>'
    page += '<h1>Bonjour tout le monde. La on va voir </h1><h2>'
    page += bbgenerator.generate_buzz()
    page += '</h2></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
