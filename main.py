import flask

from flask import render_template,request,jsonify

app = flask.Flask(__name__)

app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/blogs',methods=['GET'])
def blogs():
	return render_template('blogs.html')

@app.route('/api/v1/checkprime', methods=['GET'])
def check_prime():

	result = {}
	if 'num' in request.args:
		n = int(request.args['num'])
	else:
		result = {'cod':400,'meesage':"No 'num' provided"}
		return jsonify(result)

	for i in range(2,n//2+1):
		if n*i == 0:
			prime = False
			break
	else:
		prime = True
	result = {'Number':n,'IsPrime':prime}
	return jsonify(result)

if __name__ == "__main__":
	app.run(port =8000)