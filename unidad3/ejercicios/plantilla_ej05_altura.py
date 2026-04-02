# unidad3/ejercicios/plantilla_ej05_altura.py
# Ejercicio 5 — altura() en Árbol-B
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa la función altura() abajo.
#   2. Ejecuta: python plantilla_ej05_altura.py
#
# DEFINICIÓN: la altura de un árbol con solo la raíz (hoja) es 0.
# Para árboles más altos, es la cantidad de niveles de nodos internos.
# =====================================================================

import importlib.util
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

_EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), '..', 'ejemplos', '01_arbol_b.py')
_spec = importlib.util.spec_from_file_location('arbol_b', _EXAMPLE_PATH)
_b_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_b_mod)
ArbolB = _b_mod.ArbolB
from utils.visualizar import imprimir_arbol_b


def altura(arbol: ArbolB) -> int:
    """
    Retorna la altura del árbol.
    Altura 0 = solo la raíz (o árbol vacío).

    TODO: implementa esta función.
    PISTA: en un Árbol-B todas las hojas están al mismo nivel,
           así que puedes bajar siempre por el primer hijo hasta llegar
           a una hoja y contar los pasos.
    """
    raise NotImplementedError("Implementa altura()")


# ------------------------------------------------------------------
# Caso 1: árbol vacío (solo raíz vacía) → altura 0
# ------------------------------------------------------------------
arbol_vacio = ArbolB(orden=3)
assert altura(arbol_vacio) == 0, f"Árbol vacío: esperado 0, obtenido {altura(arbol_vacio)}"

# ------------------------------------------------------------------
# Caso 2: solo la raíz (un nodo) → altura 0
# ------------------------------------------------------------------
arbol_uno = ArbolB(orden=3)
arbol_uno.insertar(5)
assert altura(arbol_uno) == 0, f"Un nodo: esperado 0, obtenido {altura(arbol_uno)}"

# ------------------------------------------------------------------
# Caso 3: insertar [3, 7, 2, 6, 5, 12, 10, 4, 9] en orden 3
# El árbol debería tener altura 1 (raíz + un nivel de hojas)
# ------------------------------------------------------------------
arbol = ArbolB(orden=3)
for v in [3, 7, 2, 6, 5, 12, 10, 4, 9]:
    arbol.insertar(v)

print("Árbol-B de orden 3:")
imprimir_arbol_b(arbol._raiz)
print()

h = altura(arbol)
assert h == 1, f"Se esperaba altura 1, se obtuvo {h}"

print("✓ Todos los tests pasaron.")
