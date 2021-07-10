import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

with open("Toxic/tokenizer.pickle", 'rb') as f:
	tokenizer = pickle.load(f)

def evaluate(sentence):
	sentence = [sentence]
	seq = tokenizer.texts_to_sequences(sentence)
	padded = np.array(pad_sequences(seq, maxlen=50, padding='post'))
	models = tf.keras.models.load_model('Toxic/best_model.h5')
	preds = models.predict([padded])
	return preds
	