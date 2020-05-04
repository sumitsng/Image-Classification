

import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense 
from google.colab.patches import cv2_imshow



(train, labelTrain), (test, labelTest)  = tf.keras.datasets.mnist.load_data(path = 'mnist.npz')
     

    
def one_hot_vector(Index):
  A = np.zeros(10)
  A[Index] = 1 
  return A

def one_hot_coding( label_list):
  A = np.empty((1,10))
  for index in label_list:
    tmp = one_hot_vector(index).reshape(1,10)
    A = np.concatenate((A,tmp ), axis = 0)
  A = np.delete(A ,0 ,0)
  return np.array(A)
    
def image_processing(self, Image):
  return float(Image)/255

def data_processing(self, Image_list):
  for index in range(0, len(Image_list)):
    Image_list[index] = image_processing(self , Image_list[index])
  return Image_list

labelTrain = one_hot_coding(labelTrain)
labelTest = one_hot_coding(labelTest)

train = train.reshape(-1,28,28,1)
test = test.reshape(-1,28,28,1)
print(train.shape, test.shape)

model = Sequential()
model.add(Convolution2D(32,3,2,activation='relu',input_shape = (28,28,1), use_bias= True,))
model.add(MaxPooling2D(3,1))
model.add(Convolution2D(64,2,1,activation='relu',use_bias=True))
model.add(Flatten())
model.add(Dense(units=10, activation='softmax'))
model.compile(optimizer= 'adam' , loss = 'categorical_crossentropy' , metrics = ['accuracy'])

model.fit( x = train , y = labelTrain , batch_size= 1000, epochs = 10 , verbose = 1  , validation_data = (test , labelTest), shuffle= True )

loss , accuracy = model.evaluate(x = test , y = labelTest , batch_size= 1000)
print(loss , accuracy)

X = model.predict(test)
print(np.argmax(X))

cv2_imshow(test[0])
