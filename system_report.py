import os
import platform
import shutil
import socket
import sys
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None


def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)


def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "No disponible"


def get_system_drive():
    if platform.system() == "Windows":
        return os.environ.get("SystemDrive", "C:") + "\\"
    return "/"


print("=" * 60)
print("REPORTE BÁSICO DEL SISTEMA - VERSIÓN 2")
print("=" * 60)

print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Equipo: {socket.gethostname()}")
print(f"IP local: {get_local_ip()}")

print("\nSISTEMA")
print(f"Sistema operativo: {platform.system()}")
print(f"Versión: {platform.version()}")
print(f"Arquitectura: {platform.machine()}")
print(f"Procesador: {platform.processor()}")
print(f"Versión de Python: {sys.version.split()[0]}")

if psutil:
    ram = psutil.virtual_memory()

    print("\nMEMORIA RAM")
    print(f"Total: {bytes_to_gb(ram.total)} GB")
    print(f"Usada: {bytes_to_gb(ram.used)} GB")
    print(f"Disponible: {bytes_to_gb(ram.available)} GB")
    print(f"Uso: {ram.percent}%")
else:
    print("\nMEMORIA RAM")
    print("No disponible.")
    print("Instala psutil con: pip install psutil")

system_drive = get_system_drive()
total, used, free = shutil.disk_usage(system_drive)

print("\nALMACENAMIENTO")
print(f"Unidad analizada: {system_drive}")
print(f"Total: {bytes_to_gb(total)} GB")
print(f"Usado: {bytes_to_gb(used)} GB")
print(f"Disponible: {bytes_to_gb(free)} GB")

print("=" * 60)
