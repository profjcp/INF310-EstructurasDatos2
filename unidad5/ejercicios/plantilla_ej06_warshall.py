# unidad5/ejercicios/plantilla_ej06_warshall.py
# Ejercicio 6 — warshall(): cierre transitivo
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa la función warshall() abajo.
#   2. Ejecuta: python plantilla_ej06_warshall.py
#
# PISTA: el algoritmo de Warshall es similar a Floyd-Warshall, pero
# la matriz almacena True/False en lugar de distancias.
# alcanzable[i][j] = True si existe algún camino (de cualquier longitud)
# de i a j, usando vértices intermedios.
#
# Inicialización: alcanzable[i][j] = True si existe arista i→j,
#                 alcanzable[i][i] = True (siempre).
# =====================================================================

import importlib.util
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

_EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), '..', 'ejemplos', '01_algoritmos_grafos_pesados.py')
_spec = importlib.util.spec_from_file_location('grafos_pesados', _EXAMPLE_PATH)
_gp_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gp_mod)
GrafoPesado = _gp_mod.GrafoPesado


def warshall(grafo: GrafoPesado) -> dict:
    """
    Algoritmo de Warshall: cierre transitivo del grafo.

    Retorna un diccionario alcanzable[i][j] = True si existe
    algún camino de i a j (incluyendo el camino trivial i→i).

    TODO: implementa esta función.
    """
    raise NotImplementedError("Implementa warshall()")


# ------------------------------------------------------------------
# Grafo del Ejercicio 1 (Unidad V):
# A→B:10  A→D:5  B→C:1  B→D:2  C→E:4  D→B:3  D→C:9  D→E:2  E→A:7  E→C:6
# ------------------------------------------------------------------
g = GrafoPesado(dirigido=True)
for u, v, w in [("A","B",10),("A","D",5),("B","C",1),("B","D",2),
                ("C","E",4),("D","B",3),("D","C",9),("D","E",2),
                ("E","A",7),("E","C",6)]:
    g.agregar_arista(u, v, w)

alcanzable = warshall(g)

print("Cierre transitivo (Warshall):")
vertices = sorted(alcanzable.keys())
print("   " + " ".join(f"{v:>3}" for v in vertices))
for i in vertices:
    fila = " ".join("  ✓" if alcanzable[i][j] else "  ✗" for j in vertices)
    print(f"{i:>2} {fila}")
print()

# En este grafo (con ciclo A→...→E→A), todos los vértices son alcanzables
# desde cualquier otro vértice.
for i in vertices:
    for j in vertices:
        assert alcanzable[i][j] is True, (
            f"Se esperaba alcanzable[{i}][{j}] = True "
            f"(el grafo es fuertemente conexo)"
        )

# ------------------------------------------------------------------
# Grafo lineal dirigido: A→B→C (sin ciclos)
# A puede llegar a B y C; B puede llegar a C; C no puede llegar a nadie
# ------------------------------------------------------------------
g2 = GrafoPesado(dirigido=True)
for u, v, w in [("A","B",1),("B","C",1)]:
    g2.agregar_arista(u, v, w)

a2 = warshall(g2)
assert a2["A"]["A"] is True
assert a2["A"]["B"] is True
assert a2["A"]["C"] is True
assert a2["B"]["A"] is False, "B no puede llegar a A sin ciclo"
assert a2["C"]["A"] is False, "C no puede llegar a A sin ciclo"

print("✓ Todos los tests pasaron.")
