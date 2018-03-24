import keras
from keras.models import model_from_json
import cv2
import os

model = model_from_json(open('model.json').read())
model.load_weights('weights.h5')


def predict(X):
	image = cv2.resize(X,(64,64), interpolation = cv2.INTER_CUBIC)
	image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	image = image.reshape(1,64,64,1)
	image = np.array([image])
	pr = model.predict(image)
	for i in range(p):
		if p[i]==max(p):
			if i == 3:
				print("Happy")
			else:
				print("Sad")

X = cv2.imread("data/testset/face5.jpeg")
p = predict(X)
print(p)