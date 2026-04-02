# unidad1/ejercicios/plantilla_ej04_contar_hojas.py
# Ejercicio 4 — contar_hojas()
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa la función contar_hojas() abajo.
#   2. Ejecuta este archivo: python plantilla_ej04_contar_hojas.py
#   3. Si todos los asserts pasan, verás "✓ Todos los tests pasaron."
# =====================================================================

import importlib.util
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

_EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), '..', 'ejemplos', '02_abb_completo.py')
_spec = importlib.util.spec_from_file_location('abb_completo', _EXAMPLE_PATH)
_abb_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_abb_mod)
ArbolBinarioBusqueda = _abb_mod.ArbolBinarioBusqueda
from utils.visualizar import imprimir_arbol


def contar_hojas(arbol: ArbolBinarioBusqueda) -> int:
    """
    Retorna la cantidad de nodos hoja en el árbol.
    Un nodo hoja es aquel que no tiene hijos (izquierdo == derecho == None).

    TODO: implementa esta función usando recursión o iteración.
    """
    raise NotImplementedError("Implementa contar_hojas()")


# ------------------------------------------------------------------
# Árbol del Ejercicio 1: inserción [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
# ------------------------------------------------------------------
abb = ArbolBinarioBusqueda()
for v in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
    abb.insertar(v)

print("Árbol resultante:")
imprimir_arbol(abb._raiz)
print()

# ------------------------------------------------------------------
# Tests automáticos
# ------------------------------------------------------------------
resultado = contar_hojas(abb)
assert resultado == 4, (
    f"Se esperaban 4 hojas (2, 9, 17, 20), pero se obtuvo {resultado}.\n"
    "Revisá tu recorrido: un nodo hoja tiene .izquierdo == .derecho == None."
)

# Árbol vacío → 0 hojas
abb_vacio = ArbolBinarioBusqueda()
assert contar_hojas(abb_vacio) == 0, "Un árbol vacío debe retornar 0 hojas."

# Árbol de un solo nodo → 1 hoja (la raíz es hoja)
abb_uno = ArbolBinarioBusqueda()
abb_uno.insertar(42)
assert contar_hojas(abb_uno) == 1, "Un árbol con un solo nodo debe retornar 1 hoja."

print("✓ Todos los tests pasaron.")
