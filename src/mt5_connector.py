import MetaTrader5 as mt5

class MT5Connector:
    TIMEFRAME_M1 = mt5.TIMEFRAME_M1
    
    def __init__(self, usuario, contraseña, servidor):
        self.usuario = usuario
        self.contraseña = contraseña
        self.servidor = servidor

    def conectar(self):
        if not mt5.initialize():
            raise Exception("Error al inicializar MetaTrader 5")

        if not mt5.login(self.usuario, password=self.contraseña, server=self.servidor):
            mt5.shutdown()
            raise Exception(f"Error al conectar con el servidor {self.servidor}")

        print("Conexión exitosa a MetaTrader 5")

    def obtener_datos_mercado(self, simbolo, timeframe, desde, hasta):
        return mt5.copy_rates_range(simbolo, timeframe, desde, hasta)

    def cerrar_conexion(self):
        mt5.shutdown()
        print("Conexión cerrada con MetaTrader 5")
