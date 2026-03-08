# ejemplos/01_pep8_convenciones.py
# Unidad 0: Estándares y Buenas Prácticas de Codificación
# =========================================================
# Este archivo demuestra las convenciones de estilo PEP 8 en Python.

# ❌ MAL: nombres poco descriptivos, sin docstrings
class n:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None

# ✅ BIEN: nombres descriptivos, docstrings, type hints
class Nodo:
    """
    Representa un nodo en un árbol binario.
    
    Atributos:
        dato: El valor almacenado en el nodo.
        izquierdo: Hijo izquierdo del nodo.
        derecho: Hijo derecho del nodo.
    """
    
    def __init__(self, dato: int):
        """Inicializa el nodo con el dato proporcionado."""
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
    
    def __repr__(self) -> str:
        """Representación legible del nodo."""
        return f"Nodo({self.dato})"
    
    def tiene_hijos(self) -> bool:
        """Retorna True si el nodo tiene al menos un hijo."""
        return self.izquierdo is not None or self.derecho is not None


# ---------------------------------------------------------------
# Convenciones de nombres
# ---------------------------------------------------------------

# Variables: snake_case
nombre_alumno = "Ana García"
cantidad_nodos = 0
esta_vacio = True

# Constantes: UPPER_SNAKE_CASE
MAX_ALTURA = 100
VALOR_DEFAULT = -1

# Funciones: snake_case, verbo descriptivo
def calcular_altura(nodo: Nodo) -> int:
    """
    Calcula la altura del subárbol con raíz en 'nodo'.
    
    Args:
        nodo: Nodo raíz del subárbol.
    
    Returns:
        Altura del subárbol. Retorna -1 si el nodo es None.
    """
    if nodo is None:
        return -1
    
    altura_izq = calcular_altura(nodo.izquierdo)
    altura_der = calcular_altura(nodo.derecho)
    
    return 1 + max(altura_izq, altura_der)


def contar_nodos(nodo: Nodo) -> int:
    """
    Cuenta la cantidad de nodos en el subárbol.
    
    Args:
        nodo: Nodo raíz del subárbol.
    
    Returns:
        Número de nodos en el subárbol.
    """
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izquierdo) + contar_nodos(nodo.derecho)


# ---------------------------------------------------------------
# Manejo de errores
# ---------------------------------------------------------------

def insertar_valor(arbol, valor: int) -> None:
    """Inserta un valor en el árbol con manejo de errores."""
    if not isinstance(valor, (int, float)):
        raise TypeError(f"Se esperaba un número, se recibió: {type(valor)}")
    
    if valor is None:
        raise ValueError("El valor no puede ser None")
    
    arbol.insertar(valor)


# ---------------------------------------------------------------
# Demo
# ---------------------------------------------------------------

if __name__ == "__main__":
    # Construir un árbol simple manualmente
    raiz = Nodo(50)
    raiz.izquierdo = Nodo(30)
    raiz.derecho = Nodo(70)
    raiz.izquierdo.izquierdo = Nodo(20)
    raiz.izquierdo.derecho = Nodo(40)

    print("=== Demo de Buenas Prácticas ===")
    print(f"Raíz: {raiz}")
    print(f"Altura del árbol: {calcular_altura(raiz)}")
    print(f"Total de nodos: {contar_nodos(raiz)}")
    print(f"La raíz tiene hijos: {raiz.tiene_hijos()}")
    print(f"El nodo 20 tiene hijos: {raiz.izquierdo.izquierdo.tiene_hijos()}")
