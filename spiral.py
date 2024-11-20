import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.optimizers import RMSprop

from Question1.utils import create_neural_network, create_test_data

EPOCHS = 250
BATCH_SIZE = 20

def create_neural_network(layers, neurons, activation, optimizer, loss, outputs=1):
    if layers != len(neurons):
        raise ValueError("Number of layers doesn't much the amount of neuron layers.")

    model = Sequential()

    for i in range(layers):
        model.add(Dense(neurons[i], activation=activation))

    # Output
    if outputs == 1:
        model.add(Dense(outputs))
    else:
        model.add(Dense(outputs, activation='softmax'))

    model.compile(optimizer=optimizer,
                  loss=loss)

    return model

def main():
    df = three_spirals(1000)

    # Set-up data
    x_train = df[['x-coord', 'y-coord']].values
    y_train = df['class'].values

    # Don't need y_test, can inspect visually if it worked or not
    x_test = create_test_data()

    # Scale data
    scaler = MinMaxScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    relu_model = create_neural_network(layers=3,
                                       neurons=[40, 40, 40],
                                       activation='relu',
                                       optimizer=RMSprop(learning_rate=0.001),
                                       loss='categorical_crossentropy',
                                       outputs=3)

    # Train networks
    relu_model.fit(x=x_train, y=y_train, epochs=EPOCHS, verbose=1, batch_size=BATCH_SIZE)

    # Predictions on test data
    relu_predictions = relu_model.predict_classes(x_test)

    models = [relu_model]
    test_predictions = [relu_predictions]

    # Plot
    plot_data(models, test_predictions)