from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import numpy as np
import sys
import os

BADE_DIR = os.path.dirname(os.path.abspath(__file__))

# Usage: python model.py croppedface_gray.jpg
# (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
batch_size = 1
img_width = 48
img_height = 48

fer_model = load_model(BADE_DIR + '/classifier_batch200_augmented_val_acc_0.5305.h5')
graph = tf.get_default_graph()

def predict(img_file):
	img = image.load_img(img_file, target_size=(img_width, img_height), grayscale=True)
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = x / 255.0

	global graph
	with graph.as_default():
		predictions = fer_model.predict(x, batch_size=batch_size)
	results = decode_predictions(predictions)

	predictions = [{'label': label, 'description': description, 'probability': probability * 100.0}
                    for label, description, probability in results[0]]
	return predictions

def decode_predictions(predictions):
	result = []
	for pred in predictions:
		row = []
		for i in range(len(pred)):
			row.append((i, emotions[i], pred[i]))
		row = sorted(row, key=lambda r: r[2], reverse=True)
		result.append(row)
	return result

def save(data, filename):
	with file(filename, 'w') as f:
		for line in data:
			np.savetxt(f, line, delimiter=',', fmt='%s')

if __name__ == "__main__":
	predictions = predict(sys.argv[1])
	print(predictions)






