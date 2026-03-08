# Unidad 0 · Estándares y Buenas Prácticas de Codificación

## 🎯 Objetivo

Aplicar estándares y buenas prácticas de codificación en Python para escribir código limpio, mantenible y profesional antes de abordar las estructuras de datos complejas.

---

## 1. Estructuras de Codificación

### 1.1 Convenciones de nombres (PEP 8)

Python tiene una guía de estilo oficial llamada **PEP 8**. Las reglas más importantes:

| Elemento | Convención | Ejemplo |
|----------|-----------|---------|
| Variables y funciones | `snake_case` | `mi_variable`, `calcular_altura()` |
| Clases | `PascalCase` | `ArbolBinario`, `NodoGrafo` |
| Constantes | `UPPER_SNAKE_CASE` | `MAX_NODOS = 100` |
| Privados | prefijo `_` | `_raiz`, `_contador` |

### 1.2 Docstrings y comentarios

```python
class Nodo:
    """
    Representa un nodo en una estructura de datos.
    
    Atributos:
        dato: El valor almacenado en el nodo.
        siguiente: Referencia al siguiente nodo.
    """
    
    def __init__(self, dato):
        """Inicializa el nodo con el dato proporcionado."""
        self.dato = dato
        self.siguiente = None
```

### 1.3 Type Hints (tipado)

A partir de Python 3.5 puedes declarar tipos, lo que mejora la legibilidad:

```python
def buscar(self, valor: int) -> bool:
    """Busca un valor en la estructura. Retorna True si lo encuentra."""
    ...

def insertar(self, dato: any) -> None:
    ...
```

---

## 2. Manejo de Interfaces (Clases Abstractas)

En Python usamos el módulo `abc` para definir interfaces o contratos:

```python
from abc import ABC, abstractmethod

class EstructuraDatos(ABC):
    """Interfaz base para todas las estructuras de datos."""
    
    @abstractmethod
    def insertar(self, dato):
        """Inserta un elemento en la estructura."""
        pass
    
    @abstractmethod
    def eliminar(self, dato):
        """Elimina un elemento de la estructura."""
        pass
    
    @abstractmethod
    def buscar(self, dato) -> bool:
        """Busca un elemento. Retorna True si existe."""
        pass
    
    @abstractmethod
    def esta_vacia(self) -> bool:
        """Retorna True si la estructura no tiene elementos."""
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """Retorna la cantidad de elementos."""
        pass
```

Luego cualquier clase que extienda `EstructuraDatos` **debe** implementar todos esos métodos:

```python
class ArbolBinario(EstructuraDatos):
    def insertar(self, dato):
        # implementación concreta
        ...
```

---

## 3. Arquitectura de un Proyecto

Una buena organización de carpetas para este curso:

```
mi_proyecto/
├── README.md
├── models/
│   ├── __init__.py
│   ├── nodo.py          ← Clase Nodo base
│   └── arbol.py         ← Clase ArbolBinario
├── utils/
│   ├── __init__.py
│   └── visualizacion.py ← Funciones auxiliares para imprimir árboles
├── tests/
│   ├── __init__.py
│   └── test_arbol.py    ← Pruebas unitarias
└── main.py              ← Punto de entrada
```

### Ejemplo de `nodo.py`

```python
# models/nodo.py

class Nodo:
    """Nodo genérico para estructuras de datos."""
    
    def __init__(self, dato):
        self.dato = dato
    
    def __repr__(self):
        return f"Nodo({self.dato})"
```

### Ejemplo de `main.py`

```python
# main.py
from models.arbol import ArbolBinario

def main():
    arbol = ArbolBinario()
    for valor in [50, 30, 70, 20, 40]:
        arbol.insertar(valor)
    
    print("Recorrido en orden:", arbol.en_orden())

if __name__ == "__main__":
    main()
```

---

## ✅ Checklist de Buenas Prácticas

Antes de entregar cualquier código, verifica:

- [ ] ¿Las clases y funciones tienen docstrings?
- [ ] ¿Los nombres son descriptivos (no `x`, `temp`, `var1`)?
- [ ] ¿El código tiene manejo de errores (`try/except`)?
- [ ] ¿Se usa `if __name__ == "__main__"` en el módulo principal?
- [ ] ¿El código está indentado con 4 espacios (no tabs)?
- [ ] ¿Las líneas no superan los 79 caracteres?

---

## 📁 Archivos de esta unidad

- [`ejemplos/01_pep8_convenciones.py`](./ejemplos/01_pep8_convenciones.py)
- [`ejemplos/02_clases_abstractas.py`](./ejemplos/02_clases_abstractas.py)
- [`ejercicios/enunciados.md`](./ejercicios/enunciados.md)
