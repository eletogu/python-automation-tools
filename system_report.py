import platform
import shutil
import socket
from datetime import datetime


def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)


print("=" * 50)
print("REPORTE BÁSICO DEL SISTEMA")
print("=" * 50)

print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Equipo: {socket.gethostname()}")
print(f"Sistema operativo: {platform.system()}")
print(f"Versión: {platform.version()}")
print(f"Arquitectura: {platform.machine()}")
print(f"Procesador: {platform.processor()}")

total, used, free = shutil.disk_usage("/")

print("\nALMACENAMIENTO")
print(f"Total: {bytes_to_gb(total)} GB")
print(f"Usado: {bytes_to_gb(used)} GB")
print(f"Disponible: {bytes_to_gb(free)} GB")

print("=" * 50)
