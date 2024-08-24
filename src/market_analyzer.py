import pandas as pd
import statsmodels.api as sm

class MarketAnalyzer:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.modelo_arima = None

    def ajustar_arima(self, order=(5,1,0)):
        self.modelo_arima = sm.tsa.ARIMA(self.data['close'], order=order)
        self.modelo_arima = self.modelo_arima.fit()

    def predecir(self, pasos=5):
        if self.modelo_arima is None:
            raise Exception("El modelo ARIMA no está ajustado.")
        return self.modelo_arima.forecast(steps=pasos)
