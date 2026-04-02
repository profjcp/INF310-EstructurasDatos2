# unidad2/ejercicios/plantilla_ej05_enorden.py
# Ejercicio 5 — recorrido_enorden() en Árbol M-Vías
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa la función recorrido_enorden() abajo.
#   2. Ejecuta: python plantilla_ej05_enorden.py
#
# PISTA (recorrido en-orden para M-vías):
#   Para un nodo con claves [k0, k1, ..., kn] e hijos [h0, h1, ..., hn]:
#     recorrer(h0), visitar k0, recorrer(h1), visitar k1, ..., recorrer(hn)
# =====================================================================

import importlib.util
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

_EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), '..', 'ejemplos', '02_arbol_mvias.py')
_spec = importlib.util.spec_from_file_location('arbol_mvias', _EXAMPLE_PATH)
_mvias_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mvias_mod)
ArbolMVias = _mvias_mod.ArbolMVias
NodoMVias = _mvias_mod.NodoMVias
from utils.visualizar import imprimir_arbol_b


def recorrido_enorden(arbol: ArbolMVias) -> list:
    """
    Retorna una lista con todas las claves del árbol en orden ascendente.

    TODO: implementa esta función con recursión.
    """
    raise NotImplementedError("Implementa recorrido_enorden()")


# ------------------------------------------------------------------
# Árbol de prueba: orden 4
#              [20, 40, 60]
#             /    |    |    \
#          [10]  [30]  [50]  [70, 80]
# ------------------------------------------------------------------
def construir_arbol_prueba():
    raiz = NodoMVias(4)
    raiz.claves = [20, 40, 60]
    h0 = NodoMVias(4); h0.claves = [10]
    h1 = NodoMVias(4); h1.claves = [30]
    h2 = NodoMVias(4); h2.claves = [50]
    h3 = NodoMVias(4); h3.claves = [70, 80]
    raiz.hijos = [h0, h1, h2, h3]
    arbol = ArbolMVias(4)
    arbol._raiz = raiz
    return arbol

arbol = construir_arbol_prueba()
print("Árbol M-Vías de orden 4:")
imprimir_arbol_b(arbol._raiz)
print()

resultado = recorrido_enorden(arbol)
esperado = [10, 20, 30, 40, 50, 60, 70, 80]
assert resultado == esperado, (
    f"Se esperaba {esperado}\n"
    f"Se obtuvo   {resultado}"
)

# Árbol vacío
arbol_vacio = ArbolMVias(3)
assert recorrido_enorden(arbol_vacio) == [], "Árbol vacío debe retornar lista vacía"

print("✓ Todos los tests pasaron.")
