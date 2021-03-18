import os
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# @app.route('/')
# def test():
# 	print('test')
# 	return 'test'

@app.route('/user-script', methods=['GET'])
def userScript():
	# print(request.args)
	filePath1 = 'C:/GitHub/Firefox-Extension/Public/UserScript/{}.js'.format(request.args['file-name'])
	filePath2 = 'C:/GitHub/Firefox-Extension/Private/UserScript/{}.js'.format(request.args['file-name'])
	if(os.path.exists(filePath1)):
		return send_file(filePath1)
	if(os.path.exists(filePath2)):
		return send_file(filePath2)
	return ''
