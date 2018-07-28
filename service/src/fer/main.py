from flask import Flask, current_app, request, jsonify
import io
import model
import base64
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter


app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

@app.route('/', methods=['POST'])
def predict():
	predictions=[]
	msg=''
	data = {}
	try:
		data = request.get_json()['data']
	except Exception:
		current_app.logger.error('Bad Request. request: %s', request)
		return jsonify(status_code='400', msg='Bad Request'), 400

	data = base64.b64decode(data)

	image = io.BytesIO(data)
	try:
		msg, predictions,ganimg = model.predict(image)
		current_app.logger.info('msg: %s', msg)
		current_app.logger.info('predictions: %s', predictions)
		current_app.logger.info('ganimg: %s', ganimg)
	except Exception:
		current_app.logger.exception('Exception in model.predict')
	return jsonify(ganimg=ganimg, predictions=predictions, msg=msg)


if __name__ == '__main__':
	handler = RotatingFileHandler('local_test.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
	app.logger.addHandler(handler)
	app.run(host='127.0.0.1', port=10080, debug=True)
