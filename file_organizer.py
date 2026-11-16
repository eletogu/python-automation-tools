from pathlib import Path
import shutil


def organize_files(folder):
    folder_path = Path(folder)

    if not folder_path.exists():
        print("La ruta indicada no existe.")
        return

    if not folder_path.is_dir():
        print("La ruta indicada no corresponde a una carpeta.")
        return

    moved_files = 0

    for file in folder_path.iterdir():

        if not file.is_file():
            continue

        extension = file.suffix.lower().replace(".", "")

        if not extension:
            extension = "sin_extension"

        destination = folder_path / extension.upper()

        destination.mkdir(exist_ok=True)

        target = destination / file.name

        if target.exists():
            stem = file.stem
            suffix = file.suffix
            counter = 1

            while target.exists():
                target = destination / f"{stem}_{counter}{suffix}"
                counter += 1

        shutil.move(str(file), str(target))
        moved_files += 1

    print(f"Organización completada.")
    print(f"Archivos movidos: {moved_files}")


folder = input("Ruta de la carpeta que deseas organizar: ").strip()

organize_files(folder)
