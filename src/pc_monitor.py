import psutil

class PCMonitor:
    def __init__(self, nombre_proceso="terminal.exe"):
        self.nombre_proceso = nombre_proceso

    def monitorear(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == self.nombre_proceso:
                proceso = psutil.Process(proc.info['pid'])
                uso_cpu = proceso.cpu_percent(interval=1)
                uso_memoria = proceso.memory_info().rss / (1024 * 1024)  # En MB
                return uso_cpu, uso_memoria
        raise Exception(f"Proceso {self.nombre_proceso} no encontrado")
