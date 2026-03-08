# Unidad I · Ejercicios: Árboles Binarios de Búsqueda

## Ejercicio 1 — Inserción manual

Dado el siguiente orden de inserción: **15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9**

a) Dibuja el ABB resultante.  
b) ¿Cuál es la altura del árbol?  
c) ¿Cuántos nodos hoja tiene?  
d) ¿Cuántos nodos tienen exactamente 1 hijo?

---

## Ejercicio 2 — Recorridos

Usando el árbol del Ejercicio 1, escribe el resultado de:

a) Recorrido en-orden  
b) Recorrido pre-orden  
c) Recorrido post-orden  
d) Recorrido por niveles  
e) ¿Qué recorrido produce la lista ordenada? ¿Por qué?

---

## Ejercicio 3 — Eliminación

Partiendo del árbol del Ejercicio 1, elimina los nodos en este orden: **4**, **7**, **15**.

Dibuja el árbol después de cada eliminación e indica qué caso de eliminación se aplicó en cada paso.

---

## Ejercicio 4 — Implementación

Agrega el siguiente método a la clase `ArbolBinarioBusqueda`:

```python
def contar_hojas(self) -> int:
    """Retorna la cantidad de nodos hoja en el árbol."""
    pass
```

Luego verifica con el árbol del Ejercicio 1 (debería tener 4 hojas: 2, 9, 13, 20... ¡comprueba!).

---

## Ejercicio 5 — Sucesor inorden

Implementa el método:

```python
def sucesor(self, dato) -> int | None:
    """
    Retorna el sucesor inorden del nodo con el dato dado.
    El sucesor inorden es el siguiente elemento en el recorrido en-orden.
    Retorna None si el dato no existe o no tiene sucesor.
    """
    pass
```

Ejemplo: para el árbol [15,6,18,3,7], `sucesor(7)` debería retornar `15`.

---

## Ejercicio 6 — Validar ABB

Implementa una función que verifique si un árbol binario arbitrario cumple la propiedad ABB:

```python
def es_abb_valido(raiz) -> bool:
    """
    Verifica que el árbol con la raíz dada sea un ABB válido.
    Pista: cada nodo debe estar dentro de un rango [min, max].
    """
    pass
```

---

## Ejercicio 7 — Aplicación: Agenda telefónica

Implementa una **Agenda Telefónica** usando un ABB donde la clave de ordenamiento es el nombre:

```python
class Contacto:
    def __init__(self, nombre: str, telefono: str):
        ...

class AgendaTelefonica:
    def agregar(self, nombre: str, telefono: str) -> None: ...
    def buscar(self, nombre: str) -> str | None: ...
    def eliminar(self, nombre: str) -> bool: ...
    def listar_alfabetico(self) -> list: ...  # usa recorrido en-orden
```

---

## 📋 Rúbrica de evaluación

| Criterio | Puntos |
|----------|--------|
| Código funciona correctamente | 40% |
| Código bien documentado (docstrings) | 20% |
| Manejo de casos borde (árbol vacío, valor no encontrado) | 20% |
| Nombres descriptivos y buenas prácticas | 20% |
