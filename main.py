import time
import os
from prometheus_client import start_http_server, Gauge
import psutil

CPU    = Gauge("sistema_cpu_percent",  "Uso de CPU em %")
RAM    = Gauge("sistema_ram_percent",  "Uso de RAM em %")
DISCO  = Gauge("sistema_disco_percent","Uso de disco em %")
DISCO_LIVRE = Gauge("sistema_disco_livre_gb", "Disco livre em GB")

def coletar():
    mem   = psutil.virtual_memory()
    disco = psutil.disk_usage("/")
    CPU.set(psutil.cpu_percent(interval=1))
    RAM.set(mem.percent)
    DISCO.set(disco.percent)
    DISCO_LIVRE.set(round(disco.free / 1024**3, 2))

    os.system("clear")
    print("=" * 40)
    print("  Monitor do sistema")
    print("=" * 40)
    print(f"  CPU:    {psutil.cpu_percent():>6.1f} %")
    print(f"  RAM:    {mem.percent:>6.1f} %")
    print(f"  Disco:  {disco.percent:>6.1f} %  (livre: {round(disco.free/1024**3,2)} GB)")
    print("=" * 40)
    print("  Metricas em: http://localhost:8000/metrics")
    print("  Ctrl+C para sair")

if __name__ == "__main__":
    start_http_server(8000)
    print("Iniciando monitor...")
    while True:
        try:
            coletar()
            time.sleep(3)
        except KeyboardInterrupt:
            print("\nEncerrado.")
            break
