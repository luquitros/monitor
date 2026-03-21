import psutil

class PsutilCollector:
    def coletar(self) -> dict:
        mem = psutil.virtual_memory()
        disco = psutil.disk_usage("/")
        return {
            "cpu_percent":    psutil.cpu_percent(interval=1),
            "ram_percent":    mem.percent,
            "ram_usado_mb":   round(mem.used / 1024**2, 1),
            "ram_total_mb":   round(mem.total / 1024**2, 1),
            "disco_percent":  disco.percent,
            "disco_usado_gb": round(disco.used / 1024**3, 2),
            "disco_livre_gb": round(disco.free / 1024**3, 2),
        }
