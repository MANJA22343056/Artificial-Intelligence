import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Contoh data latih
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_train = np.array([[0], [1], [1], [0]], dtype=np.float32)

# Contoh data uji
X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_test = np.array([[0], [1], [1], [0]], dtype=np.float32)

model = Sequential(
    [Dense(4, input_shape=(2,), activation="relu"), Dense(1, activation="sigmoid")])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")

predictions = model.predict(X_test)
print(predictions)
