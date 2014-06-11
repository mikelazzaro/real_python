# ---- Flask Hello World ----

from flask import Flask

# Create app object
app = Flask(__name__)

# define view using function, which returns string
    # Use decorators to link function to url
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, world!"

# start the dev server using the run() method

if __name__ == "__main__":
    app.run()

