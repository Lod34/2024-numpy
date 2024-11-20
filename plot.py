import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1001) ##quel +1 nel 1000 serve per inserire lo zero, altrimenti alcune funzioni come l'iperbole xy=1 risultano continue

y1 = x
y2 = 1/x
y3 = np.sqrt(x**2-2)

plt.arrow(0,-10,0,20) #asse y
plt.ylim(-10,10)
plt.arrow(-10,0,20,0) #asse x
plt.xlim(-10,10)


plt.plot(x,y1,label="y = x")
plt.plot(x,y2,label="y = (1/2)^x")
plt.plot(x,y3)

plt.title("un po' di grafici:")
plt.legend()
plt.show()


