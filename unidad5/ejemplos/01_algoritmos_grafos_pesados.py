# ejemplos/01_algoritmos_grafos_pesados.py
# Unidad V: Dijkstra, Floyd-Warshall, Warshall, Prim, Kruskal
# =============================================================

import heapq


# ==============================================================
# GRAFO PESADO
# ==============================================================

class GrafoPesado:
    """
    Grafo pesado (ponderado) con lista de adyacencia.
    Cada arista tiene un peso numérico.
    """
    
    def __init__(self, dirigido: bool = False):
        self._adyacencia = {}  # {vertice: [(vecino, peso)]}
        self.dirigido = dirigido
    
    def agregar_vertice(self, v) -> None:
        if v not in self._adyacencia:
            self._adyacencia[v] = []
    
    def agregar_arista(self, u, v, peso: float) -> None:
        """Agrega arista u→v con el peso dado."""
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self._adyacencia[u].append((v, peso))
        if not self.dirigido:
            self._adyacencia[v].append((u, peso))
    
    def vertices(self) -> list:
        return list(self._adyacencia.keys())
    
    def __str__(self) -> str:
        lineas = []
        for v in sorted(self._adyacencia, key=str):
            vecinos = [(w, p) for w, p in sorted(self._adyacencia[v], key=lambda x: str(x[0]))]
            lineas.append(f"  {v} → {vecinos}")
        return "\n".join(lineas)


# ==============================================================
# DIJKSTRA
# ==============================================================

def dijkstra(grafo: GrafoPesado, origen) -> tuple[dict, dict]:
    """
    Algoritmo de Dijkstra: camino más corto desde origen a todos los vértices.
    
    Requisito: todos los pesos deben ser >= 0.
    
    Args:
        grafo: Grafo pesado.
        origen: Vértice de partida.
    
    Returns:
        (distancias, predecesores)
        distancias: {vertice: distancia_minima_desde_origen}
        predecesores: {vertice: vertice_anterior_en_camino_optimo}
    
    Complejidad: O((V + E) log V)
    """
    INF = float('inf')
    distancias = {v: INF for v in grafo.vertices()}
    distancias[origen] = 0
    predecesores = {v: None for v in grafo.vertices()}
    
    # Cola de prioridad: (distancia_actual, vertice)
    heap = [(0, origen)]
    visitados = set()
    
    while heap:
        dist_actual, u = heapq.heappop(heap)
        
        if u in visitados:
            continue  # ya procesado (entrada obsoleta en el heap)
        visitados.add(u)
        
        # Relajar aristas salientes de u
        for vecino, peso in grafo._adyacencia.get(u, []):
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                predecesores[vecino] = u
                heapq.heappush(heap, (nueva_dist, vecino))
    
    return distancias, predecesores


def reconstruir_camino(predecesores: dict, origen, destino) -> list:
    """Reconstruye el camino óptimo desde origen hasta destino."""
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = predecesores[actual]
    camino.reverse()
    if camino[0] == origen:
        return camino
    return []  # no hay camino


# ==============================================================
# FLOYD-WARSHALL
# ==============================================================

def floyd_warshall(vertices: list, aristas: list) -> tuple[dict, dict]:
    """
    Algoritmo de Floyd-Warshall: camino más corto entre TODOS los pares.
    
    Args:
        vertices: Lista de vértices.
        aristas: Lista de tuplas (u, v, peso).
    
    Returns:
        (dist, next_hop)
        dist[i][j] = distancia mínima de i a j
        next_hop[i][j] = siguiente vértice en el camino óptimo i→j
    
    Complejidad: O(V³)
    """
    INF = float('inf')
    
    # Inicializar matrices
    dist = {i: {j: INF for j in vertices} for i in vertices}
    next_v = {i: {j: None for j in vertices} for i in vertices}
    
    for v in vertices:
        dist[v][v] = 0
    
    for u, v, w in aristas:
        dist[u][v] = w
        next_v[u][v] = v
    
    # Programación dinámica: probar todos los vértices intermedios k
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_v[i][j] = next_v[i][k]
    
    return dist, next_v


# ==============================================================
# PRIM (Árbol de Expansión Mínima)
# ==============================================================

def prim(grafo: GrafoPesado, inicio) -> list:
    """
    Algoritmo de Prim: Árbol de Expansión Mínima (MST).
    
    Crece el MST agregando la arista de menor peso que conecta
    un nuevo vértice al árbol existente.
    
    Args:
        grafo: Grafo no dirigido y pesado.
        inicio: Vértice de partida.
    
    Returns:
        Lista de aristas del MST: [(u, v, peso), ...]
    
    Complejidad: O(E log V)
    """
    visitados = {inicio}
    mst = []
    # Heap: (peso, vertice_origen, vertice_destino)
    heap = [(peso, inicio, vecino) for vecino, peso in grafo._adyacencia[inicio]]
    heapq.heapify(heap)
    
    while heap and len(visitados) < len(grafo.vertices()):
        peso, u, v = heapq.heappop(heap)
        
        if v in visitados:
            continue
        
        visitados.add(v)
        mst.append((u, v, peso))
        
        for vecino, p in grafo._adyacencia[v]:
            if vecino not in visitados:
                heapq.heappush(heap, (p, v, vecino))
    
    return mst


# ==============================================================
# KRUSKAL (Árbol de Expansión Mínima con Union-Find)
# ==============================================================

class UnionFind:
    """Estructura Union-Find (Conjuntos Disjuntos) para Kruskal."""
    
    def __init__(self, elementos):
        self.padre = {e: e for e in elementos}
        self.rango = {e: 0 for e in elementos}
    
    def encontrar(self, x):
        """Encuentra la raíz del conjunto de x (con compresión de camino)."""
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]
    
    def unir(self, x, y) -> bool:
        """Une los conjuntos de x e y. Retorna False si ya estaban unidos."""
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        
        if raiz_x == raiz_y:
            return False  # mismo componente → formaría ciclo
        
        # Unión por rango
        if self.rango[raiz_x] < self.rango[raiz_y]:
            raiz_x, raiz_y = raiz_y, raiz_x
        self.padre[raiz_y] = raiz_x
        if self.rango[raiz_x] == self.rango[raiz_y]:
            self.rango[raiz_x] += 1
        return True


def kruskal(vertices: list, aristas: list) -> list:
    """
    Algoritmo de Kruskal: Árbol de Expansión Mínima.
    
    Ordena aristas por peso y agrega las que no forman ciclo.
    
    Args:
        vertices: Lista de vértices.
        aristas: Lista de tuplas (u, v, peso).
    
    Returns:
        Lista de aristas del MST: [(u, v, peso), ...]
    
    Complejidad: O(E log E)
    """
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])
    uf = UnionFind(vertices)
    mst = []
    
    for u, v, peso in aristas_ordenadas:
        if uf.unir(u, v):
            mst.append((u, v, peso))
        
        if len(mst) == len(vertices) - 1:
            break  # MST completo
    
    return mst


# ==============================================================
# DEMO
# ==============================================================

if __name__ == "__main__":
    # ---- Dijkstra ----
    print("=" * 50)
    print("DIJKSTRA - Camino más corto")
    print("=" * 50)
    
    g = GrafoPesado(dirigido=False)
    conexiones = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('C', 'B', 1), ('C', 'D', 8),
        ('B', 'D', 5), ('B', 'E', 3),
        ('D', 'E', 2)
    ]
    for u, v, w in conexiones:
        g.agregar_arista(u, v, w)
    
    print("Grafo:")
    print(g)
    
    distancias, predecesores = dijkstra(g, 'A')
    print(f"\nDistancias desde A:")
    for v in sorted(distancias):
        camino = reconstruir_camino(predecesores, 'A', v)
        print(f"  A → {v}: {distancias[v]}  (camino: {' → '.join(camino)})")
    
    # ---- Floyd-Warshall ----
    print("\n" + "=" * 50)
    print("FLOYD-WARSHALL - Todos los pares")
    print("=" * 50)
    
    vs = ['A', 'B', 'C', 'D']
    aristas_fw = [
        ('A','B',3), ('A','C',8), ('A','D',4),
        ('B','D',1), ('C','B',4), ('D','C',2)
    ]
    dist, _ = floyd_warshall(vs, aristas_fw)
    
    print("Matriz de distancias mínimas:")
    print(f"{'':5}", end="")
    for j in vs:
        print(f"{j:8}", end="")
    print()
    for i in vs:
        print(f"{i:5}", end="")
        for j in vs:
            val = dist[i][j]
            print(f"{'∞':8}" if val == float('inf') else f"{val:8}", end="")
        print()
    
    # ---- Prim y Kruskal ----
    print("\n" + "=" * 50)
    print("PRIM y KRUSKAL - Árbol de Expansión Mínima")
    print("=" * 50)
    
    g2 = GrafoPesado(dirigido=False)
    aristas_mst = [
        ('A','B',4), ('A','H',8), ('B','C',8), ('B','H',11),
        ('C','D',7), ('C','F',4), ('C','I',2), ('D','E',9),
        ('D','F',14), ('E','F',10), ('F','G',2), ('G','H',1),
        ('G','I',6), ('H','I',7)
    ]
    vertices_mst = ['A','B','C','D','E','F','G','H','I']
    for u, v, w in aristas_mst:
        g2.agregar_arista(u, v, w)
    
    mst_prim = prim(g2, 'A')
    peso_prim = sum(w for _,_,w in mst_prim)
    print(f"\nMST - Prim (desde A):")
    for u, v, w in mst_prim:
        print(f"  {u} — {v}: {w}")
    print(f"  Peso total: {peso_prim}")
    
    mst_kruskal = kruskal(vertices_mst, aristas_mst)
    peso_kruskal = sum(w for _,_,w in mst_kruskal)
    print(f"\nMST - Kruskal:")
    for u, v, w in mst_kruskal:
        print(f"  {u} — {v}: {w}")
    print(f"  Peso total: {peso_kruskal}")
    
    print(f"\n¿Prim == Kruskal? {peso_prim == peso_kruskal} (mismo peso total)")
