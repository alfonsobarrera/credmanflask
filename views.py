


from flask import Flask, request, redirect, url_for, jsonify
import logging

app=Flask(__name__)
app.debug=True


@app.route("/")
def hello():
	return "Welcome to credman\n"
	
@app.route("/add", methods=['POST'])
def add_credential():
	dic={}

	try:
		form=request.form
		for i in form:
			dic[i]=form[i]
		
		return jsonify(dic)
	except Exception as e:
		logging.warning("Exception was detected".format(e))
		return ""

		
	
	
if __name__=="__main__":
	app.run(host='0.0.0.0')
	
