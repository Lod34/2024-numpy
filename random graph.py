import numpy as np
import matplotlib.pyplot as plt
import random

# Generare i valori di x
x_values = np.linspace(0.1, 10, 100)  # Evitare x=0 per evitare divisione per zero in y2
y_values = []

# Selezionare randomicamente una funzione per ogni valore di x
for x in x_values:
    choice = random.choice([1, 2, 3])
    if choice == 1:
        y = x  # y1 = x
    elif choice == 2:
        y = 2**x  # y2 = 1/x
    elif choice == 3:
        y = 1/x  # y3 = np.sqrt(x**2-2)
    
    y_values.append(y)

# Creare il grafico
plt.scatter(x_values, y_values, color='blue')
plt.title('Grafico cartesiano delle funzioni selezionate randomicamente')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()