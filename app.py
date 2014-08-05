import os
from flask import flask

# initialization
app = Flask(_name_)
app.config.update(
	DEBUG = True,
)


# controllers
@app.route("/")
def hello():
	return "Hello from Python!"


#lauch
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)