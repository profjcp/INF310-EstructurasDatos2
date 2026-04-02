# Unidad IV · Ejercicios: Grafos

## Ejercicio 1 — Representaciones [Básico]

Dado el siguiente grafo **no dirigido**:

```
Vértices: {A, B, C, D, E}
Aristas: A-B, A-C, B-C, B-D, C-E, D-E
```

a) Dibuja el grafo.  
b) Escribe la **lista de adyacencia** para cada vértice.  
c) Escribe la **matriz de adyacencia** (1 = arista existe, 0 = no existe).  
d) ¿Cuántas aristas tiene el grafo? ¿Cómo se relaciona esto con la suma de grados de los vértices?

---

## Ejercicio 2 — BFS manual [Básico]

Usando el grafo del Ejercicio 1, aplica **BFS** (Búsqueda en Anchura) partiendo del vértice **A**:

a) Muestra el orden de visita de los vértices.  
b) Dibuja el **árbol BFS** resultante.  
c) ¿Cuál es la distancia (en aristas) desde A hasta cada vértice?  
d) ¿Cómo usarías BFS para detectar si el grafo es conexo?

---

## Ejercicio 3 — DFS manual [Básico]

Usando el mismo grafo, aplica **DFS** (Búsqueda en Profundidad) partiendo del vértice **A**:

a) Muestra el orden de visita con DFS recursivo.  
b) Muestra el orden de visita con DFS iterativo (usando pila).  
c) ¿Los resultados son siempre idénticos? ¿Por qué?  
d) ¿Cómo usarías DFS para detectar ciclos en un grafo dirigido?

---

## Ejercicio 4 — Grafo dirigido y orden topológico [Intermedio]

Representá las siguientes materias y sus prerrequisitos como un **grafo dirigido** (arista A→B significa "A es prerrequisito de B"):

```
INF110 → INF220
INF110 → MAT210
INF220 → INF310
MAT210 → INF310
INF310 → INF410
MAT210 → MAT310
```

a) Dibuja el grafo dirigido.  
b) ¿Existe algún ciclo? ¿Qué implicaría un ciclo en el contexto de prerrequisitos?  
c) Aplica el **orden topológico** (algoritmo de Kahn o DFS) y escribe una secuencia válida de cursado.  
d) ¿Existe más de una secuencia válida? Escribe otra si es posible.

---

## Ejercicio 5 — Implementación: detectar ciclos [Intermedio]

Agrega el siguiente método a la clase `Grafo`:

```python
def tiene_ciclo(self) -> bool:
    """
    Retorna True si el grafo tiene al menos un ciclo, False si es acíclico.
    Para grafos no dirigidos: usar DFS con seguimiento del padre.
    Para grafos dirigidos: usar DFS con estados (blanco/gris/negro).
    """
    pass
```

---

## Ejercicio 6 — Implementación: orden topológico [Desafío]

Agrega a la clase `Grafo`:

```python
def orden_topologico(self) -> list | None:
    """
    Retorna una lista de vértices en orden topológico.
    Retorna None si el grafo tiene ciclos (no es un DAG).
    Usar el algoritmo de Kahn (por grados de entrada).
    """
    pass
```

Verifica con el grafo del Ejercicio 4 que el resultado sea una secuencia de cursado válida.

---

## 📋 Rúbrica de evaluación

| Criterio | Puntos |
|----------|--------|
| Código funciona correctamente | 40% |
| Código bien documentado (docstrings) | 20% |
| Manejo de casos borde (grafo vacío, vértice aislado) | 20% |
| Nombres descriptivos y buenas prácticas | 20% |
