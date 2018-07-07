from flask import Flask, render_template, request, jsonify, Blueprint
import ocr

app = Flask(__name__)

@app.route('/imgurl/<url>', methods=['GET'])
def index(url):
	ocr.config(url)
	text = ocr.getFinalText()
	response_object = {
		'status': 'success',
		'data': {
			'text': text
			}
	}
	return jsonify(response_object), 202

if __name__ == '__main__':
	app.run(debug=True)