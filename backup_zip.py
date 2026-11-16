import shutil
from pathlib import Path
from datetime import datetime


def create_backup(source):
    source_path = Path(source)

    if not source_path.exists():
        print("La ruta indicada no existe.")
        return

    if not source_path.is_dir():
        print("La ruta indicada no corresponde a una carpeta.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_name = f"backup_{source_path.name}_{timestamp}"

    destination = source_path.parent / backup_name

    print("Creando copia de seguridad...")
    print(f"Origen: {source_path}")

    shutil.make_archive(
        str(destination),
        "zip",
        root_dir=str(source_path)
    )

    print("\nCopia creada correctamente.")
    print(f"Archivo generado: {destination}.zip")


folder = input("Ruta de la carpeta que deseas respaldar: ").strip()

create_backup(folder)
