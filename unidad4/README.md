# Unidad IV · Grafos

**Tiempo estimado:** 18 horas

## 🎯 Objetivo

Representar e implementar los Grafos mediante estructuras estáticas (matrices) y dinámicas (listas de adyacencia), y aplicar los algoritmos fundamentales de recorrido.

---

## 1. Conceptos Básicos y Terminología

### ¿Qué es un Grafo?

Un **grafo** G = (V, E) es una estructura matemática formada por:
- **V** = conjunto de **vértices** (nodos)
- **E** = conjunto de **aristas** (edges) que conectan pares de vértices

```
Ejemplo de grafo no dirigido:

    A --- B
    |   / |
    |  /  |
    | /   |
    C --- D

Vértices: {A, B, C, D}
Aristas: {(A,B), (A,C), (B,C), (B,D), (C,D)}
```

### Terminología esencial

| Término | Definición |
|---------|-----------|
| **Vértice / Nodo** | Elemento del grafo |
| **Arista / Arco** | Conexión entre dos vértices |
| **Grado** | Número de aristas que inciden en un vértice |
| **Camino** | Secuencia de vértices conectados por aristas |
| **Ciclo** | Camino que empieza y termina en el mismo vértice |
| **Grafo conexo** | Existe camino entre cualquier par de vértices |
| **Grafo acíclico** | No contiene ciclos |
| **Grafo completo (Kₙ)** | Cada vértice está conectado con todos los demás |
| **Subgrafo** | Subconjunto de vértices y aristas del grafo original |

---

## 2. Grafos Dirigidos (Digrafos)

En un **grafo dirigido**, cada arista tiene una **dirección**. La arista (A→B) es diferente de (B→A).

```
Grafo dirigido:

    A ──→ B
    ↑   ↙ ↓
    |  ↙  |
    C ←── D

Aristas: A→B, B→C, D→B, D→C, C→A
```

- **In-grado** de un vértice: número de aristas que llegan a él.
- **Out-grado** de un vértice: número de aristas que salen de él.

---

## 3. Grafos No Dirigidos

Las aristas no tienen dirección. (A,B) = (B,A).

```
    A --- B --- D
    |     |
    C ----+
```

---

## 4. Representación Computacional

### 4.1 Matriz de Adyacencia

Una matriz n×n donde `M[i][j] = 1` si existe arista entre vértice i y vértice j.

```
Grafo: A-B, A-C, B-D, C-D

     A  B  C  D
A  [ 0  1  1  0 ]
B  [ 1  0  0  1 ]
C  [ 1  0  0  1 ]
D  [ 0  1  1  0 ]
```

**Ventajas:** Verificar si existe arista → O(1)  
**Desventajas:** Espacio O(V²), ineficiente para grafos dispersos

### 4.2 Lista de Adyacencia

Un diccionario donde cada vértice apunta a la lista de sus vecinos.

```python
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

**Ventajas:** Espacio O(V + E), eficiente para grafos dispersos  
**Desventajas:** Verificar arista → O(grado del vértice)

---

## 5. Recorrido de Grafos

### 5.1 Búsqueda en Amplitud (BFS - Breadth First Search)

Visita primero todos los vecinos del nodo inicial, luego los vecinos de los vecinos, etc. Usa una **cola**.

```
BFS desde A en:
    A --- B --- D
    |     |
    C ----+

Cola: [A]
Visitar A → Cola: [B, C]
Visitar B → Cola: [C, D]
Visitar C → Cola: [D]
Visitar D → Cola: []

Orden de visita: A, B, C, D
```

**Aplicación:** Encontrar el **camino más corto** (en número de aristas) entre dos vértices.

### 5.2 Búsqueda en Profundidad (DFS - Depth First Search)

Va tan profundo como puede antes de retroceder. Usa recursión (o una **pila**).

```
DFS desde A:

Orden de visita: A, B, D, C
```

**Aplicación:** Detectar ciclos, componentes conexas, ordenamiento topológico.

---

## 6. Ordenamiento Topológico

El **ordenamiento topológico** de un grafo dirigido acíclico (DAG) es una ordenación lineal de los vértices tal que para cada arista (u→v), u aparece antes que v.

```
Prerrequisitos de materias:
    Prog1 → Prog2 → ED1 → ED2
    Prog1 → Matemáticas → ED2

Ordenamiento topológico válido:
    Prog1, Prog2, Matemáticas, ED1, ED2
```

**Algoritmo:** DFS con pila (al terminar de visitar un nodo, apilarlo).

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_grafo_matriz.py`](./ejemplos/01_grafo_matriz.py) | Grafo con matriz de adyacencia |
| [`ejemplos/02_grafo_lista.py`](./ejemplos/02_grafo_lista.py) | Grafo con lista de adyacencia |
| [`ejemplos/03_bfs_dfs.py`](./ejemplos/03_bfs_dfs.py) | BFS y DFS completos |
| [`ejemplos/04_orden_topologico.py`](./ejemplos/04_orden_topologico.py) | Ordenamiento topológico |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
