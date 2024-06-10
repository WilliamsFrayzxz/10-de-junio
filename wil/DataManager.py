import pandas as pd

class DataManager:
    def __init__(self):
        self.data = None

    def cargar_datos(self, archivo):
        self.data = pd.read_csv(archivo)

    def obtener_primeras_10_filas(self):
        return self.data.head(10)

    def calcular_estadisticas(self):
        return self.data.describe()

    # Otros métodos para análisis, visualización, etc.