# -*- coding: utf-8 -*-
"""K49_JAPANESE_CNN_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13ezD33whmPveAViQqwX8SG1URKhynMe3
"""

from google.colab import drive
drive.mount('/content/gdrive')
# Imports
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras import layers
from keras import Sequential
from sklearn.model_selection import train_test_split

# Paths
drive_path = '/content/gdrive/MyDrive/Colab Notebooks/japanese_datset/k49'
train_imgs_path = os.path.join(drive_path, 'k49-train-imgs.npz')
train_labels_path = os.path.join(drive_path, 'k49-train-labels.npz')
test_imgs_path = os.path.join(drive_path, 'k49-test-imgs.npz')
test_labels_path = os.path.join(drive_path, 'k49-test-labels.npz')

# Data loading
X_train = np.load(train_imgs_path)['arr_0']
Y_train= np.load(train_labels_path)['arr_0']
X_test= np.load(test_imgs_path)['arr_0']
Y_test= np.load(test_labels_path)['arr_0']

X_train = X_train.reshape(232365,28,28,1)

X_test = X_test.reshape(38547,28,28,1)

X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.10)

Y_train = keras.utils.to_categorical(Y_train)
Y_test= keras.utils.to_categorical(Y_test)
Y_val=keras.utils.to_categorical(Y_val)

model = Sequential()

model.add(layers.Conv2D(32, (3, 3), strides=(1, 1), activation='relu', input_shape=(28,28,1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.3))

model.add(layers.Conv2D(64, (3, 3), strides=(1, 1), activation='relu'))
model.add(layers.Conv2D(64, (3, 3), strides=(1, 1), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.3))

model.add(layers.Conv2D(96, (3, 3), strides=(1, 1), activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.3))

model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(49, activation='softmax'))




model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])



# Let's look at our model
model.summary()

model.fit(X_train, Y_train, epochs=25,validation_data=(X_val, Y_val), batch_size=128)

