import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("a.csv")
print(datos.head(5))
print(datos.tail(5))
print(datos.info())
print(datos.describe())
print(datos.columns)
print(datos.index)

