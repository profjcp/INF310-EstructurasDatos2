# Unidad V · Grafos Pesados y Algoritmos Clásicos

**Tiempo estimado:** 12 horas

## 🎯 Objetivo

Resolver problemas de la vida real que se solucionan con los algoritmos clásicos de los grafos pesados.

---

## 1. Conceptualización

### ¿Qué es un Grafo Pesado?

Un **grafo pesado** (o ponderado) es un grafo donde cada arista tiene un **peso** (costo, distancia, tiempo, etc.) asociado.

```
Red de ciudades con distancias en km:

    A ---50--- B
    |         /|
   30        / |
    |       80 |
   60       /  |
    |      /   40
    C ---70--- D

Aristas:
  A-B: 50 km
  A-C: 30 km  (¡más corta que ir directo A-B si continuamos!)
  A-D: 60 km
  B-D: 40 km
  C-D: 70 km
  B-C: 80 km
```

### Representación computacional

**Matriz de pesos:**
```
     A    B    C    D
A  [ 0   50   30   60  ]
B  [ 50   0   80   40  ]
C  [ 30  80    0   70  ]
D  [ 60  40   70    0  ]
```
(∞ si no existe arista directa)

**Lista de adyacencia con pesos:**
```python
grafo = {
    'A': [('B', 50), ('C', 30), ('D', 60)],
    'B': [('A', 50), ('C', 80), ('D', 40)],
    'C': [('A', 30), ('B', 80), ('D', 70)],
    'D': [('A', 60), ('B', 40), ('C', 70)]
}
```

---

## 2. Algoritmo de Dijkstra (Shortest Path)

### Problema

Dado un vértice fuente s, encontrar el **camino de menor costo** desde s hasta todos los demás vértices.

### Condición: no funciona con pesos negativos.

### Idea del algoritmo

```
1. Inicializar: distancia[s] = 0, distancia[v] = ∞ para todos los demás.
2. Usar una cola de prioridad (min-heap) con (distancia, vértice).
3. Mientras la cola no esté vacía:
   a. Extraer el vértice u con menor distancia actual.
   b. Para cada vecino v de u:
      - Si distancia[u] + peso(u,v) < distancia[v]:
        → Actualizar distancia[v] y agregar a la cola ("relajar" la arista)
```

### Ejemplo paso a paso

```
Grafo: A→B(4), A→C(2), B→D(5), C→B(1), C→D(8), B→E(3), D→E(2)
Fuente: A

Paso 0: dist = {A:0, B:∞, C:∞, D:∞, E:∞}
        Cola: [(0,A)]

Paso 1: Extraer A(0). Vecinos: B(4), C(2)
        dist = {A:0, B:4, C:2, D:∞, E:∞}
        Cola: [(2,C), (4,B)]

Paso 2: Extraer C(2). Vecinos: B(2+1=3 < 4!), D(2+8=10)
        dist = {A:0, B:3, C:2, D:10, E:∞}
        Cola: [(3,B), (4,B_obsoleto), (10,D)]

Paso 3: Extraer B(3). Vecinos: D(3+5=8 < 10!), E(3+3=6)
        dist = {A:0, B:3, C:2, D:8, E:6}
        
...continúa hasta vaciar la cola

Resultado final: A→A:0, A→C:2, A→B:3, A→E:6, A→D:8
Caminos: A→C, A→C→B, A→C→B→E, A→C→B→D
```

**Complejidad:** O((V + E) log V) con min-heap.

---

## 3. Algoritmos Clásicos

### 3.1 Algoritmo de Floyd-Warshall

Encuentra el **camino más corto entre todos los pares** de vértices.

```python
# Para cada vértice intermedio k:
for k in vertices:
    for i in vertices:
        for j in vertices:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**Complejidad:** O(V³) — más lento que Dijkstra pero para todos los pares.

### 3.2 Algoritmo de Warshall (Cierre Transitivo)

Determina si existe **algún camino** (no el más corto) entre cada par de vértices.

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            alcanzable[i][j] = alcanzable[i][j] or (alcanzable[i][k] and alcanzable[k][j])
```

### 3.3 Árbol de Expansión Mínima (MST)

Un **MST** es un subgrafo que conecta todos los vértices con el **mínimo costo total**, sin ciclos.

**Aplicación real:** Diseño de redes de telecomunicaciones, tuberías, carreteras.

#### Algoritmo de Prim

Crece el MST vértice por vértice. Siempre agrega la arista de menor peso que conecta un vértice nuevo al árbol actual.

```
1. Empezar desde cualquier vértice.
2. Repetir hasta incluir todos los vértices:
   a. Encontrar la arista de menor peso que conecta el MST con un vértice no incluido.
   b. Agregar ese vértice y arista al MST.
```

#### Algoritmo de Kruskal

Ordena todas las aristas por peso y las agrega al MST si no forman ciclo.

```
1. Ordenar todas las aristas por peso (ascendente).
2. Para cada arista (u,v,w):
   a. Si u y v están en componentes distintas → agregar al MST.
   b. Si están en la misma componente → ignorar (formaría ciclo).
3. Usar Union-Find para detectar componentes.
```

---

## 4. Aplicaciones

| Algoritmo | Problema que resuelve | Ejemplo real |
|-----------|----------------------|-------------|
| Dijkstra | Camino más corto desde un origen | GPS, routing de paquetes |
| Floyd-Warshall | Camino más corto entre todos los pares | Tablas de routing, análisis de redes |
| Warshall | ¿Hay camino entre A y B? | Análisis de dependencias |
| Prim | Árbol de expansión mínima | Diseño de redes eléctricas |
| Kruskal | Árbol de expansión mínima | Cables de internet en una ciudad |

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_dijkstra.py`](./ejemplos/01_dijkstra.py) | Algoritmo de Dijkstra |
| [`ejemplos/02_floyd_warshall.py`](./ejemplos/02_floyd_warshall.py) | Floyd-Warshall y Warshall |
| [`ejemplos/03_prim_kruskal.py`](./ejemplos/03_prim_kruskal.py) | Prim y Kruskal (MST) |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
