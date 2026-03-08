# Unidad V · Ejercicios: Grafos Pesados

## Ejercicio 1 — Dijkstra manual

Dado el siguiente grafo pesado dirigido:

```
A→B: 10
A→D: 5
B→C: 1
B→D: 2
C→E: 4
D→B: 3
D→C: 9
D→E: 2
E→A: 7
E→C: 6
```

a) Aplica el algoritmo de Dijkstra con origen A y muestra la tabla de distancias paso a paso.  
b) Indica el camino más corto de A a C, y de A a E.  
c) ¿Cuál es la distancia mínima de A a cada vértice?

---

## Ejercicio 2 — Floyd-Warshall

Dado el grafo del ejercicio 1:

a) Construye la matriz de distancias inicial D⁰.  
b) Muestra la evolución de la matriz después de procesar cada vértice intermedio (D¹, D², ...).  
c) ¿Para qué pares de vértices cambia el camino mínimo al usar vértices intermedios?

---

## Ejercicio 3 — Árbol de Expansión Mínima

Dado el siguiente grafo no dirigido con pesos:

```
Vértices: {1, 2, 3, 4, 5, 6}
Aristas:
  1-2: 6   1-3: 1   1-4: 5
  2-3: 5   2-5: 3
  3-4: 5   3-5: 6   3-6: 4
  4-6: 2
  5-6: 6
```

a) Aplica el algoritmo de **Prim** partiendo del vértice 1.  
b) Aplica el algoritmo de **Kruskal**.  
c) ¿El MST es único? ¿Por qué?  
d) ¿Cuál es el peso total del MST?

---

## Ejercicio 4 — Problema de transporte

Una empresa de logística tiene depósitos en las ciudades: **SCZ, LPZ, CBB, ORU, PTS, TJA**.

Las distancias (en cientos de km) entre ciudades conectadas son:

| Origen | Destino | Distancia |
|--------|---------|-----------|
| SCZ | CBB | 5 |
| SCZ | LPZ | 9 |
| CBB | LPZ | 4 |
| CBB | ORU | 3 |
| LPZ | ORU | 2 |
| LPZ | PTS | 8 |
| ORU | PTS | 6 |
| ORU | TJA | 7 |
| PTS | TJA | 4 |

Implementa en Python y responde:

a) ¿Cuál es la ruta más corta entre SCZ y TJA?  
b) ¿Cuál sería la red de carreteras de costo mínimo que conecte todas las ciudades? (MST)  
c) ¿Cuál es la distancia mínima entre **todas** las ciudades (usa Floyd-Warshall)?

---

## Ejercicio 5 — Comparación de algoritmos

Completa la siguiente tabla comparativa:

| | Dijkstra | Floyd-Warshall | Warshall | Prim | Kruskal |
|-|----------|----------------|----------|------|---------|
| **¿Qué resuelve?** | | | | | |
| **Complejidad** | | | | | |
| **¿Funciona con pesos negativos?** | | | | | |
| **Tipo de grafo** | | | | | |
| **Estructura de datos clave** | | | | | |

---

## Ejercicio 6 — Extensión de código

Agrega a la clase `GrafoPesado` el método:

```python
def warshall(self) -> dict:
    """
    Algoritmo de Warshall: cierre transitivo.
    
    Returns:
        alcanzable[i][j] = True si existe algún camino de i a j
    """
    pass
```

Verifica con el grafo del ejercicio 1.
