# unidad1/ejercicios/plantilla_ej06_validar_abb.py
# Ejercicio 6 — Validar si un árbol binario es un ABB válido
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa la función es_abb_valido() abajo.
#   2. Ejecuta: python plantilla_ej06_validar_abb.py
#
# PISTA: no basta comparar cada nodo con sus hijos directos.
#   Necesitás propagar un rango [min_val, max_val] hacia abajo.
#   Raíz: rango (-∞, +∞)
#   Hijo izquierdo: rango (-∞, padre.dato)
#   Hijo derecho:   rango (padre.dato, +∞)
# =====================================================================

import importlib.util
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

_EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), '..', 'ejemplos', '02_abb_completo.py')
_spec = importlib.util.spec_from_file_location('abb_completo', _EXAMPLE_PATH)
_abb_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_abb_mod)
Nodo = _abb_mod.Nodo
from utils.visualizar import imprimir_arbol


def es_abb_valido(raiz) -> bool:
    """
    Verifica que el árbol binario con la raíz dada sea un ABB válido.

    Retorna True si cumple la propiedad ABB, False en caso contrario.

    TODO: implementa esta función con el enfoque de rangos.
    """
    raise NotImplementedError("Implementa es_abb_valido()")


# ------------------------------------------------------------------
# Árbol válido: ABB correcto
# ------------------------------------------------------------------
#        10
#       /  \
#      5   15
#     / \
#    3   7
raiz_valida = Nodo(10)
raiz_valida.izquierdo = Nodo(5)
raiz_valida.derecho = Nodo(15)
raiz_valida.izquierdo.izquierdo = Nodo(3)
raiz_valida.izquierdo.derecho = Nodo(7)

print("Árbol válido:")
imprimir_arbol(raiz_valida)
assert es_abb_valido(raiz_valida) is True, "Debería ser ABB válido"

# ------------------------------------------------------------------
# Árbol inválido: el 12 está en el subárbol izquierdo de 10,
# pero 12 > 10 → viola la propiedad ABB.
# ------------------------------------------------------------------
#        10
#       /  \
#      5   15
#     / \
#    3   12   ← ¡INVÁLIDO! 12 > 10 pero está a la izquierda de 10
raiz_invalida = Nodo(10)
raiz_invalida.izquierdo = Nodo(5)
raiz_invalida.derecho = Nodo(15)
raiz_invalida.izquierdo.izquierdo = Nodo(3)
raiz_invalida.izquierdo.derecho = Nodo(12)  # violación

print("\nÁrbol inválido (12 viola la propiedad ABB):")
imprimir_arbol(raiz_invalida)
assert es_abb_valido(raiz_invalida) is False, "Debería ser ABB inválido"

# Árbol vacío → válido por definición
assert es_abb_valido(None) is True, "Árbol vacío es ABB válido"

# Nodo único → siempre válido
assert es_abb_valido(Nodo(42)) is True, "Nodo único siempre es ABB válido"

print("\n✓ Todos los tests pasaron.")
