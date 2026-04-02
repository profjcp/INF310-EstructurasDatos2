# unidad4/ejercicios/plantilla_ej05_ciclos.py
# Ejercicio 5 — tiene_ciclo()
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa la función tiene_ciclo() abajo.
#   2. Ejecuta: python plantilla_ej05_ciclos.py
#
# PISTAS:
#   Grafo NO dirigido: DFS desde cada nodo no visitado.
#     → Un ciclo existe si encontrás un vecino ya visitado que NO es
#       el padre directo del nodo actual.
#   Grafo DIRIGIDO: DFS con 3 estados por nodo:
#     - 0 = no visitado (blanco)
#     - 1 = en pila de llamadas actual (gris) ← ciclo si encontrás uno
#     - 2 = completamente procesado (negro)
# =====================================================================

import importlib.util
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

_EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), '..', 'ejemplos', '02_grafo_lista.py')
_spec = importlib.util.spec_from_file_location('grafo_lista', _EXAMPLE_PATH)
_grafo_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_grafo_mod)
Grafo = _grafo_mod.Grafo
from utils.visualizar import imprimir_grafo


def tiene_ciclo(grafo: Grafo) -> bool:
    """
    Retorna True si el grafo tiene al menos un ciclo.

    TODO: implementa esta función.
    """
    raise NotImplementedError("Implementa tiene_ciclo()")


# ------------------------------------------------------------------
# Test 1: grafo NO dirigido — con ciclo
# A-B-C-A forma un triángulo
# ------------------------------------------------------------------
g_ciclo = Grafo(dirigido=False)
for arista in [("A", "B"), ("B", "C"), ("C", "A"), ("C", "D")]:
    g_ciclo.agregar_arista(*arista)

print("Grafo no dirigido CON ciclo:")
imprimir_grafo(g_ciclo._adyacencia)
assert tiene_ciclo(g_ciclo) is True, "Debería detectar ciclo A-B-C-A"

# ------------------------------------------------------------------
# Test 2: grafo NO dirigido — árbol (sin ciclo)
# A-B, A-C, C-D
# ------------------------------------------------------------------
g_arbol = Grafo(dirigido=False)
for arista in [("A", "B"), ("A", "C"), ("C", "D")]:
    g_arbol.agregar_arista(*arista)

print("\nGrafo no dirigido SIN ciclo (árbol):")
imprimir_grafo(g_arbol._adyacencia)
assert tiene_ciclo(g_arbol) is False, "Un árbol no tiene ciclos"

# ------------------------------------------------------------------
# Test 3: grafo DIRIGIDO — con ciclo
# A→B→C→A
# ------------------------------------------------------------------
g_dir_ciclo = Grafo(dirigido=True)
for arista in [("A", "B"), ("B", "C"), ("C", "A")]:
    g_dir_ciclo.agregar_arista(*arista)

print("\nGrafo dirigido CON ciclo:")
imprimir_grafo(g_dir_ciclo._adyacencia)
assert tiene_ciclo(g_dir_ciclo) is True, "Debería detectar ciclo A→B→C→A"

# ------------------------------------------------------------------
# Test 4: grafo DIRIGIDO — DAG (sin ciclo), como malla de prerrequisitos
# ------------------------------------------------------------------
g_dag = Grafo(dirigido=True)
for arista in [("INF110", "INF220"), ("INF110", "MAT210"),
               ("INF220", "INF310"), ("MAT210", "INF310"),
               ("INF310", "INF410")]:
    g_dag.agregar_arista(*arista)

print("\nGrafo dirigido SIN ciclo (DAG de materias):")
imprimir_grafo(g_dag._adyacencia)
assert tiene_ciclo(g_dag) is False, "Un DAG no tiene ciclos"

# Grafo vacío → sin ciclo
assert tiene_ciclo(Grafo()) is False, "Grafo vacío no tiene ciclos"

print("\n✓ Todos los tests pasaron.")
