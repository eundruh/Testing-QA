import re
import unittest

# Funciones a probar

def validar_nombre(nombre):
    # El nombre debe tener solo letras y puede contener un espacio (para nombres compuestos)
    if not nombre:
        return False
    if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombre):
        return False
    return True

def validar_email(email):
    # Verifica que el email siga el formato 'usuario@dominio.com'
    if not email:
        return False
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return False
    return True

def validar_contraseña(contraseña):
    # Requiere al menos 8 caracteres, una letra mayúscula y un número
    if len(contraseña) < 8:
        return False
    if not re.search(r"[A-Z]", contraseña):  # Al menos una letra mayúscula
        return False
    if not re.search(r"\d", contraseña):    # Al menos un número
        return False
    return True

# Base de datos simulada
usuarios_registrados = {"juan@dominio.com", "maria@dominio.com"}

def registrar_usuario(email):
    if email in usuarios_registrados:
        return "Email ya registrado"
    usuarios_registrados.add(email)
    return "Registro exitoso"

# Clases de prueba unitaria

class TestValidaciones(unittest.TestCase):

    # Test para validar nombre
    def test_nombre_valido(self):
        self.assertTrue(validar_nombre("Juan Pérez"))  # Nombre válido
        self.assertFalse(validar_nombre("Juan123"))    # Contiene números
        self.assertFalse(validar_nombre(""))           # Cadena vacía
        self.assertFalse(validar_nombre("Juan@Pérez")) # Contiene un carácter especial
        self.assertTrue(validar_nombre("Ana María"))   # Nombre compuesto válido

    # Test para validar email
    def test_email_valido(self):
        self.assertTrue(validar_email("juan@dominio.com"))
        self.assertFalse(validar_email("juan@dominio"))  # Formato incorrecto
        self.assertFalse(validar_email("juan@.com"))     # Falta dominio
        self.assertTrue(validar_email("juan@dominio.org"))
        self.assertFalse(validar_email("juan@dominio#com"))  # Carácter no permitido

    # Test para validar contraseña
    def test_contraseña_valida(self):
        self.assertTrue(validar_contraseña("Contraseña123"))   # Contraseña válida
        self.assertFalse(validar_contraseña("123"))            # Demasiado corta
        self.assertFalse(validar_contraseña("password"))       # Sin mayúsculas ni número
        self.assertTrue(validar_contraseña("Contraseña!2025")) # Válida con caracteres especiales
        self.assertFalse(validar_contraseña("Contraseña"))     # Sin número

    # Test para verificar duplicados de email
    def test_email_duplicado(self):
        self.assertEqual(registrar_usuario("juan@dominio.com"), "Email ya registrado")
        self.assertEqual(registrar_usuario("pedro@dominio.com"), "Registro exitoso")
        self.assertEqual(registrar_usuario("juan@dominio.com"), "Email ya registrado")

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
