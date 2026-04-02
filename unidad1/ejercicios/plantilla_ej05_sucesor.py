# unidad1/ejercicios/plantilla_ej05_sucesor.py
# Ejercicio 5 — sucesor inorden
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa la función sucesor() abajo.
#   2. Ejecuta: python plantilla_ej05_sucesor.py
#   3. Si todos los asserts pasan verás "✓ Todos los tests pasaron."
#
# PISTA: El sucesor inorden de un nodo X es...
#   - Si X tiene subárbol derecho: el mínimo del subárbol derecho.
#   - Si no: el ancestro más bajo cuyo hijo izquierdo es antepasado de X.
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


def sucesor(arbol: ArbolBinarioBusqueda, dato) -> int | None:
    """
    Retorna el sucesor inorden del nodo que contiene `dato`.

    El sucesor inorden es el siguiente elemento en el recorrido en-orden
    (es decir, el siguiente valor más grande).

    Retorna None si el dato no existe en el árbol, o si es el mayor.

    TODO: implementa esta función.
    """
    raise NotImplementedError("Implementa sucesor()")


# ------------------------------------------------------------------
# Árbol base: [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
# En-orden: 2, 3, 4, 6, 7, 9, 13, 15, 17, 18, 20
# ------------------------------------------------------------------
abb = ArbolBinarioBusqueda()
for v in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
    abb.insertar(v)

print("Árbol (recorrido en-orden = lista ordenada):")
imprimir_arbol(abb._raiz)
print()

# ------------------------------------------------------------------
# Tests automáticos
# ------------------------------------------------------------------
assert sucesor(abb, 7) == 9,    f"sucesor(7) esperado 9, obtenido {sucesor(abb, 7)}"
assert sucesor(abb, 13) == 15,  f"sucesor(13) esperado 15, obtenido {sucesor(abb, 13)}"
assert sucesor(abb, 2) == 3,    f"sucesor(2) esperado 3, obtenido {sucesor(abb, 2)}"
assert sucesor(abb, 18) == 20,  f"sucesor(18) esperado 20, obtenido {sucesor(abb, 18)}"
assert sucesor(abb, 20) is None, "sucesor(20) debe ser None (es el máximo)"
assert sucesor(abb, 99) is None, "sucesor(99): dato inexistente debe retornar None"

print("✓ Todos los tests pasaron.")
