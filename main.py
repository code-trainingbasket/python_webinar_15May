import flask

from flask import render_template

app = flask.Flask(__name__)

app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/blogs',methods=['GET'])
def blogs():
	return render_template('blogs.html')

if __name__ == "__main__":
	app.run(port =8000)