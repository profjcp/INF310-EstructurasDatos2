# unidad5/ejercicios/plantilla_ej04_transporte.py
# Ejercicio 4 — Red de transporte Bolivia
# =====================================================================
# INSTRUCCIONES:
#   1. Completa el bloque "TUS RESPUESTAS" al final del archivo.
#   2. Ejecuta: python plantilla_ej04_transporte.py
#   3. El script verifica automáticamente las rutas más cortas.
#
# El grafo ya está construido con las ciudades del ejercicio.
# Usá las funciones dijkstra() y floyd_warshall() de la unidad 5.
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
dijkstra = _gp_mod.dijkstra
floyd_warshall = _gp_mod.floyd_warshall
reconstruir_camino = _gp_mod.reconstruir_camino
prim = _gp_mod.prim
from utils.visualizar import imprimir_grafo, imprimir_matriz


# ------------------------------------------------------------------
# Red de transporte (distancias en cientos de km)
# ------------------------------------------------------------------
red = GrafoPesado(dirigido=False)
aristas = [
    ("SCZ", "CBB", 5), ("SCZ", "LPZ", 9),
    ("CBB", "LPZ", 4), ("CBB", "ORU", 3),
    ("LPZ", "ORU", 2), ("LPZ", "PTS", 8),
    ("ORU", "PTS", 6), ("ORU", "TJA", 7),
    ("PTS", "TJA", 4),
]
for u, v, w in aristas:
    red.agregar_arista(u, v, w)

print("Red de transporte Bolivia:")
imprimir_grafo(red._adyacencia, pesos=True)
print()

# ------------------------------------------------------------------
# a) Ruta más corta entre SCZ y TJA
# ------------------------------------------------------------------
distancias, predecesores = dijkstra(red, "SCZ")
camino_scz_tja = reconstruir_camino(predecesores, "SCZ", "TJA")

print(f"a) Ruta más corta SCZ → TJA: {' → '.join(camino_scz_tja)}")
print(f"   Distancia total: {distancias['TJA']} (cientos de km)")
print()

# ------------------------------------------------------------------
# b) MST: red de carreteras de costo mínimo
# ------------------------------------------------------------------
mst = prim(red, "SCZ")
peso_mst = sum(w for _, _, w in mst)
print("b) MST (red de costo mínimo):")
for u, v, w in mst:
    print(f"   {u} — {v}: {w}")
print(f"   Peso total del MST: {peso_mst}")
print()

# ------------------------------------------------------------------
# c) Floyd-Warshall: distancias entre todos los pares
# ------------------------------------------------------------------
vertices = red.vertices()
aristas_fw = [(u, v, w) for u, v, w in aristas] + [(v, u, w) for u, v, w in aristas]
dist_fw, _ = floyd_warshall(vertices, aristas_fw)

imprimir_matriz(dist_fw, titulo="c) Matriz de distancias mínimas (Floyd-Warshall):")
print()

# ------------------------------------------------------------------
# ✏️  TUS RESPUESTAS (completa los valores)
# ------------------------------------------------------------------
RUTA_SCZ_TJA = None        # Ej: ["SCZ", "CBB", "ORU", "TJA"]
DISTANCIA_SCZ_TJA = None   # Ej: 15
PESO_MST = None            # Ej: 20
DIST_LPZ_TJA = None        # Distancia mínima de LPZ a TJA según Floyd-Warshall

# ------------------------------------------------------------------
# Verificación automática (descomentar cuando hayas completado)
# ------------------------------------------------------------------
# assert camino_scz_tja == RUTA_SCZ_TJA, f"Ruta incorrecta: {camino_scz_tja}"
# assert distancias["TJA"] == DISTANCIA_SCZ_TJA, f"Distancia incorrecta: {distancias['TJA']}"
# assert peso_mst == PESO_MST, f"Peso MST incorrecto: {peso_mst}"
# assert dist_fw["LPZ"]["TJA"] == DIST_LPZ_TJA, f"Distancia LPZ→TJA incorrecta: {dist_fw['LPZ']['TJA']}"
# print("✓ Todos los valores son correctos.")
