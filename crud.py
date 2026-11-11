import json
import os

ARCHIVO_DATOS = 'productos.json'

def inicializar_archivo():
    """Crea el archivo JSON si no existe."""
    if not os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'w') as f:
            json.dump({}, f)

def cargar_datos():
    """Carga los datos del archivo JSON."""
    inicializar_archivo()
    with open(ARCHIVO_DATOS, 'r') as f:
        return json.load(f)

def guardar_datos(datos):
    """Guarda los datos en el archivo JSON."""
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(datos, f, indent=4)

def crear_producto(id_prod, nombre, descripcion, precio, cantidad):
    """Crea un nuevo producto. Falla si el ID ya existe."""
    datos = cargar_datos()
    if str(id_prod) in datos:
        return False, "Error: El producto con este ID ya existe."
    
    datos[str(id_prod)] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad
    }
    guardar_datos(datos)
    return True, "Producto creado exitosamente."

def leer_producto(id_prod):
    """Lee un producto específico por su ID."""
    datos = cargar_datos()
    if str(id_prod) not in datos:
        return False, "Error: Producto no encontrado."
    return True, datos[str(id_prod)]

def actualizar_producto(id_prod, nombre=None, descripcion=None, precio=None, cantidad=None):
    """Actualiza los datos de un producto existente."""
    datos = cargar_datos()
    if str(id_prod) not in datos:
        return False, "Error: No se puede actualizar, el producto no existe."
    
    if nombre is not None: datos[str(id_prod)]["nombre"] = nombre
    if descripcion is not None: datos[str(id_prod)]["descripcion"] = descripcion
    if precio is not None: datos[str(id_prod)]["precio"] = precio
    if cantidad is not None: datos[str(id_prod)]["cantidad"] = cantidad
    
    guardar_datos(datos)
    return True, "Producto actualizado exitosamente."

def eliminar_producto(id_prod):
    """Elimina un producto por su ID."""
    datos = cargar_datos()
    if str(id_prod) not in datos:
        return False, "Error: No se puede eliminar, el producto no existe."
    
    del datos[str(id_prod)]
    guardar_datos(datos)
    return True, "Producto eliminado exitosamente."