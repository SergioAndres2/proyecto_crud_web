import unittest
import os
import crud

class TestCRUDProductos(unittest.TestCase):

    def setUp(self):
        """Prepara el entorno antes de cada prueba usando un archivo temporal."""
        crud.ARCHIVO_DATOS = 'test_productos.json'
        if os.path.exists(crud.ARCHIVO_DATOS):
            os.remove(crud.ARCHIVO_DATOS)
        crud.inicializar_archivo()

    def tearDown(self):
        """Limpia el entorno después de cada prueba."""
        if os.path.exists(crud.ARCHIVO_DATOS):
            os.remove(crud.ARCHIVO_DATOS)

    # Pruebas para Crear
    def test_crear_producto_exito(self):
        exito, msj = crud.crear_producto(1, "PC", "PC gaming", 1500.0, 5)
        self.assertTrue(exito)
        self.assertEqual(msj, "Producto creado exitosamente.")

    def test_crear_producto_error(self):
        crud.crear_producto(1, "PC", "PC gaming", 1500.0, 5)
        exito, msj = crud.crear_producto(1, "Mouse", "Mouse óptico", 20.0, 10)
        self.assertFalse(exito)
        self.assertEqual(msj, "Error: El producto con este ID ya existe.")

    # Pruebas para Leer 
    def test_leer_producto_exito(self):
        crud.crear_producto(2, "Teclado", "Teclado mecánico", 100.0, 15)
        exito, datos = crud.leer_producto(2)
        self.assertTrue(exito)
        self.assertEqual(datos["nombre"], "Teclado")

    def test_leer_producto_error(self):
        exito, msj = crud.leer_producto(99)
        self.assertFalse(exito)
        self.assertEqual(msj, "Error: Producto no encontrado.")

    # Pruebas para Actualizar
    def test_actualizar_producto_exito(self):
        crud.crear_producto(3, "Monitor", "Monitor 24 pulgadas", 200.0, 8)
        exito, msj = crud.actualizar_producto(3, precio=220.0, cantidad=10)
        self.assertTrue(exito)
        _, datos = crud.leer_producto(3)
        self.assertEqual(datos["precio"], 220.0)

    def test_actualizar_producto_error(self):
        exito, msj = crud.actualizar_producto(99, precio=500.0)
        self.assertFalse(exito)
        self.assertEqual(msj, "Error: No se puede actualizar, el producto no existe.")

    # Pruebas para Eliminar
    def test_eliminar_producto_exito(self):
        crud.crear_producto(4, "Audífonos", "Inalámbricos", 80.0, 20)
        exito, msj = crud.eliminar_producto(4)
        self.assertTrue(exito)
        exito_lectura, _ = crud.leer_producto(4)
        self.assertFalse(exito_lectura)

    def test_eliminar_producto_error(self):
        exito, msj = crud.eliminar_producto(99)
        self.assertFalse(exito)
        self.assertEqual(msj, "Error: No se puede eliminar, el producto no existe.")

if __name__ == '__main__':
    unittest.main()