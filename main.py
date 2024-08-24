from src.mt5_connector import MT5Connector
from src.pc_monitor import PCMonitor
from src.market_analyzer import MarketAnalyzer
from src.prometheus_metrics import start_metrics_server, actualizar_metricas

def main():
    # Cargar configuración
    usuario = "tu_usuario"
    contraseña = "tu_contraseña"
    servidor = "tu_servidor"

    # Iniciar Prometheus para exportar métricas
    start_metrics_server()

    # Conectar a MT5
    mt5_conector = MT5Connector(usuario, contraseña, servidor)
    mt5_conector.conectar()
    
    # Monitorear PC
    pc_monitor = PCMonitor()
    cpu, memoria = pc_monitor.monitorear()

    # Analizar mercado
    datos_mercado = mt5_conector.obtener_datos_mercado("EURUSD", mt5_conector.TIMEFRAME_M1, "2023-01-01", "2023-01-31")
    analyzer = MarketAnalyzer(datos_mercado)
    analyzer.ajustar_arima()
    predicciones = analyzer.predecir()

    # Actualizar métricas
    actualizar_metricas(cpu, memoria)
    
    # Log de predicciones
    print(f"Predicciones: {predicciones}")
    print(f"Uso de CPU: {cpu}%, Memoria: {memoria} MB")

    # Finalizar conexión
    mt5_conector.cerrar_conexion()

if __name__ == "__main__":
    main()
