import numpy as np


list = [1,2,3,4,5]
array = np.array(list)
print(type(array))
print(array)
print(list)

list2 = [[1,2,3,4,5],[6,7,8,9,10]]
array2 = np.array(list2)
print(array2)

array3= np.arange(2,12,2)
print(array3)

matrizCeros = np.zeros((4,5))
print(matrizCeros)
matrizUnos = np.ones((3, 3))
print(matrizUnos)

matriz = np.linspace(2, 6, 40)
print(matriz)

matrizIdentidad = np.eye(7)
print(matrizIdentidad)

matrizRandom = np.random.random((2,3))
print(matrizRandom)

matrizAleatoriaNormal = np.random.randn(5)
print(matrizAleatoriaNormal)

matrizAleatoriaEnteros = np.random.randint(1, 51, 20)
print(matrizAleatoriaEnteros)

arrayA = np.random.randint(1,201,30)
print(arrayA)
matriz = arrayA.reshape(5, 6)
print(matriz)

arrayB= np.random.randint(1, 901, 200)
print(arrayB)
maximo = arrayB.max()
print(f"El valor maximo es {maximo}")
print(f"Se encuentra en la posicion = {arrayB.argmax()}")
minimo = arrayB.min()
print(f"El valor minimo es {minimo}")
print(f"Se encuentra en la posicion = {arrayB.argmin()}")

arrayC = np.arange(1,11)
print(arrayC)
print(arrayC[3])
print(arrayC[5:])
print(arrayC[:6])

arrayC2 = arrayC.copy()
print(arrayC2)
print(arrayC)
print("\n")
arrayC2[0]=999999
print(arrayC2)
print(arrayC)

#Video 96 minuto 31