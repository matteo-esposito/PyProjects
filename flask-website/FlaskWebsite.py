# --------------------------------#
#     Fall 2018 | Flask Website   #
# --------------------------------#

from flask import Flask

app = Flask(__name__)

# Url to get to page
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
	app.run()