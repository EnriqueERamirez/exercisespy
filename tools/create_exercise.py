import os
import argparse

def crear_estructura(ejercicio_nombre):
    os.makedirs(f"{ejercicio_nombre}/src", exist_ok=True)
    os.makedirs(f"{ejercicio_nombre}/tests/casos_de_prueba", exist_ok=True)

    with open(f"{ejercicio_nombre}/src/__init__.py", "w") as f:
        pass

    with open(f"{ejercicio_nombre}/src/{ejercicio_nombre}.py", "w") as f:
        f.write(f"def {ejercicio_nombre}(entrada):\n")
        f.write("    # Tu código va aquí\n")
        f.write("    pass\n")

    with open(f"{ejercicio_nombre}/tests/__init__.py", "w") as f:
        pass

    with open(f"{ejercicio_nombre}/tests/test_{ejercicio_nombre}.py", "w") as f:
        f.write("import unittest\n")
        f.write(f"from src.{ejercicio_nombre} import {ejercicio_nombre}\n\n")
        f.write("class TestEjercicio(unittest.TestCase):\n")
        f.write("    # Tus pruebas van aquí\n")
        f.write("\nif __name__ == '__main__':\n")
        f.write("    unittest.main()\n")

    with open(f"{ejercicio_nombre}/tests/casos_de_prueba/caso1.json", "w") as f:
        f.write("{\n")
        f.write('    "entrada": "ejemplo",\n')
        f.write('    "salida_esperada": "resultado"\n')
        f.write("}\n")

def main():
    parser = argparse.ArgumentParser(description="Crea una plantilla para un nuevo ejercicio de algoritmia.")
    parser.add_argument("nombre", help="Nombre del ejercicio")
    args = parser.parse_args()

    crear_estructura(args.nombre)

if __name__ == "__main__":
    main()
