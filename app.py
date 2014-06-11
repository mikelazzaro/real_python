# ---- Flask Hello World ----

from __future__ import print_function

import sys

from flask import Flask

# Create app object
app = Flask(__name__)

# Turn on debugging
app.config["DEBUG"] = True

# define view using function, which returns string
    # Use decorators to link function to url
@app.route("/hello")
@app.route("/")
def hello_world():
    return "Hello, world!i?!?!?!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
#    return "Search"
    return search_query

# start the dev server using the run() method

if __name__ == "__main__":
#    app.run(debug=True)
    app.run()
    sys.exit(0)

