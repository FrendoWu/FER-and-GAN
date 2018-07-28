from keras.models import load_model
from keras.preprocessing import image
from flask import current_app
import tensorflow as tf
import subprocess
import numpy as np
import sys
import os
import time
import cv2 
from PIL import Image
import glob
import base64

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Usage: python model.py croppedface_gray.jpg
# (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
batch_size = 1
img_width = 48
img_height = 48

face_cascade = cv2.CascadeClassifier(BASE_DIR + '/haarcascade_frontalface_default.xml')
fer_model = load_model(BASE_DIR + '/classifier_batch200_augmented_val_acc_0.5305.h5')
graph = tf.get_default_graph()

def predict(img_file):
	msg = ''
	predictions = []

	img = image.load_img(img_file, grayscale=True)
	img = image.img_to_array(img)
	img = np.array(img, dtype='uint8')
	faces = face_cascade.detectMultiScale(img, 1.3, 5)
	current_app.logger.info('Found %s face(s) by face_cascade.' % len(faces))

	ori_path="../StarGAN/data/ori"
	ori_full=ori_path+"/0.jpg"
	cvim=cv2.imdecode(img,cv2.IMREAD_COLOR)
	cv2.imwrite(ori_full, img)
	sh_re=os.system("../StarGAN/run.sh")
	if(sh_re==0):
		print("sh success!")
	else:
		print("sh fail")
	
	# sh_re=os.system("../StarGAN/run_jp.sh")
	# if(sh_re==0):
	# 	print("sh_jp success!")
	# else:
	# 	print("sh_jp fail")
	
#
	if len(faces) == 0:
		msg = 'No face was found!'
		return msg, predictions
	else:
		faces = sorted(faces, key=lambda face: face[3], reverse=True)
		(x,y,w,h) = faces[0]
		img = img[y:y+h, x:x+w]

	x = cv2.resize(img, (img_width, img_height))
	x = x.reshape((1, 48, 48, 1))
	x = x / 255.0

	global graph
	with graph.as_default():
		predictions = fer_model.predict(x, batch_size=batch_size)
	results = decode_predictions(predictions)

	if results[0][0][0] == 0:
		msg = 'It is an \"Angry\" face!'
	else:
		msg = 'It is a \"%s\" face!' % results[0][0][1]
	predictions = [{'label': label, 'description': description, 'probability': probability * 100.0}
                    for label, description, probability in results[0]]
	with open('/home/wings/temp/ferwebapp/fer-service/src/StarGAN/stargan_celeba_128/results/1-images.jpg', 'rb') as fin:
		image_data = fin.read()
		ganimg = base64.b64encode(image_data)
	return msg, predictions,str(ganimg)

def decode_predictions(predictions):
	result = []
	for pred in predictions:
		row = []
		for i in range(len(pred)):
			row.append((i, emotions[i], pred[i]))
		row = sorted(row, key=lambda r: r[2], reverse=True)
		result.append(row)
	return result


def genetrate_new(img_file,input_vec):
	return 0


if __name__ == "__main__":
	input_im=predict(sys.argv[1])
	predictions = predict(input_im)
	print(predictions)
#	sh_re = os.system('../StarGAN/run.sh')	

	

	 

	





