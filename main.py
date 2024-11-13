import numpy as np

array1 = np.array([1,2,3])
print("a1",array1)

array2 = np.linspace(0,100,21) #21 perché va considerato lo 0
print("a2",array2)

array3 = np.zeros(9)
print("a3",array3)

array4 = np.ones(12)
print("a4",array4)

np.random.seed(18) #il seme può essere utile per salvare i test
random1 = np.random.rand(2,3) #per il completamento automatico è preferibile premere 'tab' che 'enter'
#random1 = np.random.rand(2,3)  #per alzare il tetto di generazione da 1 a 15

print("random1",random1)

r2=random1.reshape(3,2) #il reshape deve essere compatibile altrimenti darà errore
print("random2",r2)