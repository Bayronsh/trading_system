from prometheus_client import start_http_server, Gauge

cpu_gauge = Gauge('pc_cpu_usage', 'Uso de CPU')
memoria_gauge = Gauge('pc_memory_usage', 'Uso de Memoria')

def start_metrics_server():
    start_http_server(8000)

def actualizar_metricas(cpu, memoria):
    cpu_gauge.set(cpu)
    memoria_gauge.set(memoria)
