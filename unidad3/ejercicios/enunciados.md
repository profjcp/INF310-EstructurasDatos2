# Unidad III · Ejercicios: Árbol-B

## Ejercicio 1 — Propiedades del Árbol-B [Básico]

Para un Árbol-B de **orden m = 5** (grado mínimo t = 3):

a) ¿Cuál es el número mínimo y máximo de claves por nodo (excepto la raíz)?  
b) ¿Cuál es el número mínimo y máximo de hijos por nodo interno?  
c) ¿Qué garantía ofrece el Árbol-B que **no** ofrece un árbol M-Vías sin control?  
d) Si el árbol tiene altura `h`, ¿cuántos nodos como mínimo puede tener?  
   (Fórmula: n ≥ 2t^h - 1)

---

## Ejercicio 2 — Inserción y split manual [Básico]

Dado un Árbol-B vacío de **orden 3** (t = 2, máx 2 claves, mín 1 clave por nodo),
inserta en orden: **10, 20, 5, 6, 12, 30, 7, 17**

a) Dibuja el árbol después de cada inserción.  
b) ¿En qué pasos ocurre un **split (división)**? Describe el split.  
c) ¿Cuántas veces creció la altura del árbol?

---

## Ejercicio 3 — Búsqueda en Árbol-B [Básico]

Usando el árbol resultante del Ejercicio 2:

a) Traza la búsqueda de la clave **17** (indica nodo visitado y posición).  
b) Traza la búsqueda de la clave **11** (que no existe).  
c) ¿Cuántos nodos se accedieron en cada caso? ¿Cómo se relaciona esto con la altura?

---

## Ejercicio 4 — Comparación ABB vs Árbol-B [Intermedio]

| Característica | ABB (peor caso) | Árbol-B orden 100 |
|----------------|-----------------|-------------------|
| Altura para n = 1.000.000 | ≈ n (árbol degenerado) | ≈ log₁₀₀(n) = ? |
| Accesos a disco por búsqueda | n | ? |
| ¿Garantiza balanceo? | No | Sí |

a) Completa la tabla.  
b) ¿Por qué los sistemas de archivos y bases de datos usan Árboles-B y no ABBs?  
c) Si cada nodo del Árbol-B ocupa exactamente un bloque de disco (4 KB),
   ¿cuántas claves entran en un nodo si cada clave ocupa 16 bytes?

---

## Ejercicio 5 — Implementación: altura del árbol [Intermedio]

Agrega el siguiente método a la clase `ArbolB`:

```python
def altura(self) -> int:
    """
    Retorna la altura del árbol.
    La altura de un árbol con solo la raíz (hoja) es 0.
    """
    pass
```

Verifica que después de insertar [3, 7, 2, 6, 5, 12, 10, 4, 9] en un Árbol-B de orden 3, la altura sea 1.

---

## Ejercicio 6 — Recorrido en-orden del Árbol-B [Desafío]

Agrega a la clase `ArbolB`:

```python
def recorrido_enorden(self) -> list:
    """Retorna todas las claves del árbol en orden ascendente."""
    pass
```

Verifica que el resultado esté siempre ordenado, independientemente del orden de inserción.

---

## 📋 Rúbrica de evaluación

| Criterio | Puntos |
|----------|--------|
| Código funciona correctamente | 40% |
| Código bien documentado (docstrings) | 20% |
| Manejo de casos borde (árbol vacío, un solo nodo) | 20% |
| Nombres descriptivos y buenas prácticas | 20% |
