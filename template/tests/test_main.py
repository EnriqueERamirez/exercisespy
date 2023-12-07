import unittest
from src.main import main_program

def cargar_casos_de_prueba(archivo):
    casos = []
    with open(archivo, 'r') as file:
        contenido = file.read().split('\n\n')
    
    for caso in contenido:
        partes = caso.split('\n')
        id_caso = partes[0].replace('# Caso ', '').strip()
        descripcion = partes[1].split(': ')[1].strip()
        entrada = partes[2].split(': ')[1].strip()
        salida_esperada = partes[3].split(': ')[1].strip()
        casos.append({'id': id_caso, 'descripcion': descripcion, 'entrada': entrada, 'salida_esperada': salida_esperada})

    return casos

class TestMain(unittest.TestCase):
    def test_casos(self):
        # Cargar los datos de prueba del archivo de texto
        casos = cargar_casos_de_prueba('test_cases/caso1.txt')
        
        # Iterar a través de cada caso de prueba
        for caso in casos:
            with self.subTest(id=caso["id"]):
                # Llamar a la función principal con los datos de prueba
                resultado = main_program(caso['entrada'])
                
                # Verificar si el resultado es el esperado
                self.assertEqual(resultado, caso['salida_esperada'])
    def test_otro_caso(self):
        # Este es un ejemplo de otro caso de prueba
        entrada_especifica = "datos de entrada específicos"
        salida_esperada = "resultado esperado"
        resultado = main_program(entrada_especifica)
        self.assertEqual(resultado, salida_esperada)
# Agrega más métodos de prueba según sea necesario para cubrir diferentes casos

if __name__ == '__main__':
    unittest.main()

