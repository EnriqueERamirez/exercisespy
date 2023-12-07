import os
import shutil
import argparse

def copiar_y_renombrar(plantilla_dir, nuevo_ejercicio):
    # Copiar el directorio de la plantilla
    destino_dir = f"{nuevo_ejercicio}"
    shutil.copytree(plantilla_dir, destino_dir)

    # Renombrar archivos y modificar su contenido si es necesario
    os.rename(f"{destino_dir}/src/ejercicio_plantilla.py", f"{destino_dir}/src/{nuevo_ejercicio}.py")
    os.rename(f"{destino_dir}/tests/test_ejercicio_plantilla.py", f"{destino_dir}/tests/test_{nuevo_ejercicio}.py")

    # Aquí puedes agregar más lógica para modificar el contenido de los archivos si es necesario

def main():
    parser = argparse.ArgumentParser(description="Crea un nuevo ejercicio basado en una plantilla.")
    parser.add_argument("nombre", help="Nombre del nuevo ejercicio")
    parser.add_argument("-p", "--plantilla", help="Directorio de la plantilla", default="plantilla_ejercicio")
    
    args = parser.parse_args()

    copiar_y_renombrar(args.plantilla, args.nombre)

if __name__ == "__main__":
    main()

