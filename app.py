import os
# from flask import Flask
from BBGen import bbgenerator

#appli = Flask(__name__)


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    body = ['<!DOCTYPE html><html><meta charset="utf-8">',
            '<title>It works</title><h1>It works!</h1>']
    return [line.encode('utf-8') for line in body]

app = application

#@appli.route("/")
#def generate_buzz():
#    page = '<html><body>'
#    page += '<h1>Bonjour tout le monde! La on va voir oupas</h1><h2>'
#    #page += bbgenerator.generate_buzz()
#    page += '</h2></body></html>'
#    return page

#if __name__ == "__main__":
#    appli.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
