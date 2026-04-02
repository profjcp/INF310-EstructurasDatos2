# utils/visualizar.py
# Unidad transversal: Funciones para visualizar árboles y grafos en consola
# =========================================================================
# Uso desde cualquier unidad:
#   import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
#   from utils.visualizar import imprimir_arbol, imprimir_grafo


# ------------------------------------------------------------------
# Árboles Binarios (Unidad I)
# ------------------------------------------------------------------

def imprimir_arbol(raiz, nivel: int = 0, prefijo: str = "Raíz: ") -> None:
    """
    Imprime un árbol binario rotado 90° en consola (izquierda = hoja más
    profunda, derecha = raíz).

    Compatible con cualquier nodo que tenga atributos:
        .dato, .izquierdo, .derecho

    Ejemplo de salida para ABB [50, 30, 70]:
        Raíz: 50
        ├── D: 70
        └── I: 30

    Args:
        raiz: Nodo raíz del árbol (o subárbol).
        nivel: Nivel de indentación (0 = raíz). No cambiar en llamadas externas.
        prefijo: Etiqueta que se muestra antes del valor del nodo.
    """
    if raiz is None:
        return
    sangria = "    " * nivel
    print(f"{sangria}{prefijo}{raiz.dato}")
    if raiz.izquierdo or raiz.derecho:
        if raiz.derecho:
            imprimir_arbol(raiz.derecho, nivel + 1, "├── D: ")
        else:
            print(f"{'    ' * (nivel + 1)}├── D: (vacío)")
        if raiz.izquierdo:
            imprimir_arbol(raiz.izquierdo, nivel + 1, "└── I: ")
        else:
            print(f"{'    ' * (nivel + 1)}└── I: (vacío)")


# ------------------------------------------------------------------
# Árboles M-Vías y Árbol-B (Unidades II y III)
# ------------------------------------------------------------------

def imprimir_arbol_b(raiz, nivel: int = 0) -> None:
    """
    Imprime un Árbol-B o M-Vías en formato jerárquico.

    Compatible con nodos que tengan atributos:
        .claves (list), .hijos (list)

    Ejemplo de salida para Árbol-B de orden 3 con claves [10, 20, 30, 40]:
        [20]
          [10]
          [30, 40]

    Args:
        raiz: NodoB o NodoMVias raíz.
        nivel: Nivel de indentación (0 = raíz). No cambiar en llamadas externas.
    """
    if raiz is None:
        return
    sangria = "  " * nivel
    print(f"{sangria}{raiz.claves}")
    for hijo in raiz.hijos:
        if hijo is not None:
            imprimir_arbol_b(hijo, nivel + 1)


# ------------------------------------------------------------------
# Grafos (Unidades IV y V)
# ------------------------------------------------------------------

def imprimir_grafo(adyacencia: dict, pesos: bool = False) -> None:
    """
    Imprime la lista de adyacencia de un grafo en formato legible.

    Args:
        adyacencia: Diccionario {vertice: [vecinos]} o
                    {vertice: [(vecino, peso)]} si pesos=True.
        pesos: True si los valores del diccionario son tuplas (vecino, peso).

    Ejemplo sin pesos:
        A → [B, C]
        B → [C]

    Ejemplo con pesos:
        A → B(5)  C(2)
        B → C(8)
    """
    for vertice in sorted(adyacencia, key=str):
        vecinos = adyacencia[vertice]
        if pesos:
            partes = [f"{v}({w})" for v, w in sorted(vecinos, key=lambda x: str(x[0]))]
            print(f"  {vertice} → {('  '.join(partes)) or '(sin aristas)'}")
        else:
            destinos = sorted(vecinos, key=str)
            print(f"  {vertice} → {destinos or '(sin aristas)'}")


def imprimir_matriz(matriz: dict, titulo: str = "") -> None:
    """
    Imprime una matriz de distancias (Floyd-Warshall) de forma tabulada.

    Args:
        matriz: Diccionario {i: {j: valor}}.
        titulo: Título opcional para la tabla.
    """
    vertices = sorted(matriz.keys(), key=str)
    ancho = max(len(str(v)) for v in vertices) + 2
    INF = float('inf')

    if titulo:
        print(f"\n{titulo}")
    encabezado = " " * ancho + "".join(f"{str(v):>{ancho}}" for v in vertices)
    print(encabezado)
    print("-" * len(encabezado))
    for i in vertices:
        fila = f"{str(i):>{ancho}}"
        for j in vertices:
            val = matriz[i][j]
            celda = "∞" if val == INF else str(val)
            fila += f"{celda:>{ancho}}"
        print(fila)
