import os

class Config:
    INTERVALO_SEGUNDOS = int(os.getenv("INTERVALO", 3))
    DISCO_ALVO         = os.getenv("DISCO", "sda")
