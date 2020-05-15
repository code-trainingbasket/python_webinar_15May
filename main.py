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
		result = {'cod':400,'message':"No 'num' provided"}
		return jsonify(result)

	for i in range(2,n//2+1):
		if n*i == 0:
			prime = False
			break
	else:
		prime = True
	result = {'Number':n,'IsPrime':prime,'cod':200}
	return jsonify(result)

def wordmeaning(word):
	import json
	from difflib import get_close_matches
	global w
	with open ('data.json') as f:
		data = json.load(f)
	word = word.lower()
	if word in data:
		return(data[word])
	elif word.title() in data:
		word = word.title()
		return(data[word])
	elif word.upper() in data:
		word = word.upper()
		return(data[word])
	elif len(get_close_matches(word,list(data.keys())))>0:
		w = get_close_matches(word,list(data.keys()))[0]
		return(w,data[w])
	else:
		return("Word doesn't Exist")

@app.route('/api/v1/resources/meaning' , methods=['GET'])
def word_api():

	if 'word' in request.args:
		w = request.args['word']
	else:
		result = {
				'cod':400,
				'message':"No 'word' provided",
				}
		return jsonify(result)

	m = wordmeaning(w)
	if type(m) == tuple:
			w = m[0]
			m = m[1]
	if "Word doesn't Exist" in m:
		cod = 404
	else:
		cod = 200
	result = {'word':w,'meaning':m,'cod':cod}

	return jsonify(result)

@app.route('/api/v1/resources/lcm' , methods=['GET'])
def lcm_api():

	if 'num1' in request.args:
		num1 = request.args['num1']
		num1 = int(num1)
	else:
		result = {'cod':400,'message':"No 'num1' provided"}
		return jsonify(result)

	if 'num2' in request.args:
		num2 = request.args['num2']
		num2 = int(num2)
	else:
		result = {'cod':400,'message':"No 'num2' provided"}
		return jsonify(result)

	m = n =  max(num1,num2)
	while True:
		if m % num1 == 0 and m % num2 == 0:
			lcm = m
			break
		m += n
	result = {'num1':num1,'num2':num2, 'LCM':lcm,'cod':200}

	return jsonify(result)