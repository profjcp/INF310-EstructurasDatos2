# ejemplos/02_grafo_lista.py
# Unidad IV: Grafos - Lista de Adyacencia con BFS y DFS
# ======================================================

from collections import deque


class Grafo:
    """
    Grafo implementado con lista de adyacencia (diccionario).
    
    Soporta grafos dirigidos y no dirigidos.
    
    Complejidades:
        - Agregar vértice: O(1)
        - Agregar arista: O(1)
        - BFS/DFS: O(V + E)
        - Espacio: O(V + E)
    """
    
    def __init__(self, dirigido: bool = False):
        """
        Args:
            dirigido: True para grafo dirigido, False para no dirigido.
        """
        self._adyacencia = {}   # {vertice: [vecinos]}
        self.dirigido = dirigido
    
    # ------------------------------------------------------------------
    # Construcción del grafo
    # ------------------------------------------------------------------
    
    def agregar_vertice(self, v) -> None:
        """Agrega un vértice al grafo (si no existe)."""
        if v not in self._adyacencia:
            self._adyacencia[v] = []
    
    def agregar_arista(self, u, v) -> None:
        """
        Agrega una arista entre u y v.
        Si el grafo es no dirigido, agrega también v → u.
        Si los vértices no existen, los crea automáticamente.
        """
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        if v not in self._adyacencia[u]:
            self._adyacencia[u].append(v)
        
        if not self.dirigido and u not in self._adyacencia[v]:
            self._adyacencia[v].append(u)
    
    def eliminar_arista(self, u, v) -> bool:
        """Elimina la arista u-v. Retorna True si existía."""
        if u not in self._adyacencia or v not in self._adyacencia[u]:
            return False
        self._adyacencia[u].remove(v)
        if not self.dirigido:
            self._adyacencia[v].remove(u)
        return True
    
    # ------------------------------------------------------------------
    # Consultas básicas
    # ------------------------------------------------------------------
    
    def existe_arista(self, u, v) -> bool:
        """Verifica si existe la arista u→v."""
        return u in self._adyacencia and v in self._adyacencia[u]
    
    def vecinos(self, v) -> list:
        """Retorna la lista de vecinos del vértice v."""
        return self._adyacencia.get(v, [])
    
    def grado(self, v) -> int:
        """Retorna el grado del vértice v."""
        return len(self._adyacencia.get(v, []))
    
    def vertices(self) -> list:
        """Retorna la lista de todos los vértices."""
        return list(self._adyacencia.keys())
    
    def num_vertices(self) -> int:
        return len(self._adyacencia)
    
    def num_aristas(self) -> int:
        total = sum(len(v) for v in self._adyacencia.values())
        return total if self.dirigido else total // 2
    
    # ------------------------------------------------------------------
    # BFS - Búsqueda en Amplitud
    # ------------------------------------------------------------------
    
    def bfs(self, inicio) -> list:
        """
        Recorrido BFS (Breadth First Search) desde el vértice inicio.
        Usa una cola FIFO.
        
        Returns:
            Lista de vértices en el orden en que fueron visitados.
        
        Complejidad: O(V + E)
        """
        if inicio not in self._adyacencia:
            return []
        
        visitados = set()
        orden_visita = []
        cola = deque([inicio])
        visitados.add(inicio)
        
        while cola:
            vertice = cola.popleft()
            orden_visita.append(vertice)
            
            for vecino in sorted(self._adyacencia[vertice]):  # sorted para resultados consistentes
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return orden_visita
    
    def camino_mas_corto(self, inicio, fin) -> list | None:
        """
        Encuentra el camino más corto (en número de aristas) usando BFS.
        
        Returns:
            Lista de vértices que forman el camino, o None si no existe.
        """
        if inicio not in self._adyacencia or fin not in self._adyacencia:
            return None
        if inicio == fin:
            return [inicio]
        
        visitados = {inicio: None}  # vertice → vértice anterior
        cola = deque([inicio])
        
        while cola:
            actual = cola.popleft()
            for vecino in self._adyacencia[actual]:
                if vecino not in visitados:
                    visitados[vecino] = actual
                    if vecino == fin:
                        # Reconstruir el camino
                        return self._reconstruir_camino(visitados, inicio, fin)
                    cola.append(vecino)
        
        return None  # No hay camino
    
    def _reconstruir_camino(self, predecesores: dict, inicio, fin) -> list:
        """Reconstruye el camino usando el diccionario de predecesores."""
        camino = []
        actual = fin
        while actual is not None:
            camino.append(actual)
            actual = predecesores[actual]
        return list(reversed(camino))
    
    # ------------------------------------------------------------------
    # DFS - Búsqueda en Profundidad
    # ------------------------------------------------------------------
    
    def dfs(self, inicio) -> list:
        """
        Recorrido DFS (Depth First Search) desde el vértice inicio.
        Versión recursiva.
        
        Returns:
            Lista de vértices en el orden en que fueron visitados.
        
        Complejidad: O(V + E)
        """
        if inicio not in self._adyacencia:
            return []
        
        visitados = set()
        orden_visita = []
        self._dfs_rec(inicio, visitados, orden_visita)
        return orden_visita
    
    def _dfs_rec(self, v, visitados: set, orden: list) -> None:
        visitados.add(v)
        orden.append(v)
        for vecino in sorted(self._adyacencia[v]):
            if vecino not in visitados:
                self._dfs_rec(vecino, visitados, orden)
    
    def tiene_ciclo(self) -> bool:
        """
        Detecta si el grafo (dirigido) tiene ciclos usando DFS.
        Usa coloreado de nodos: blanco=no visitado, gris=en proceso, negro=terminado.
        """
        COLOR_BLANCO, COLOR_GRIS, COLOR_NEGRO = 0, 1, 2
        color = {v: COLOR_BLANCO for v in self._adyacencia}
        
        def dfs_ciclo(v) -> bool:
            color[v] = COLOR_GRIS
            for vecino in self._adyacencia[v]:
                if color[vecino] == COLOR_GRIS:
                    return True  # arista al gris = ciclo
                if color[vecino] == COLOR_BLANCO and dfs_ciclo(vecino):
                    return True
            color[v] = COLOR_NEGRO
            return False
        
        for v in self._adyacencia:
            if color[v] == COLOR_BLANCO:
                if dfs_ciclo(v):
                    return True
        return False
    
    def orden_topologico(self) -> list | None:
        """
        Calcula el ordenamiento topológico usando DFS.
        Solo válido para grafos dirigidos acíclicos (DAG).
        
        Returns:
            Lista de vértices en orden topológico, o None si hay ciclo.
        """
        if not self.dirigido:
            return None
        if self.tiene_ciclo():
            return None
        
        visitados = set()
        pila = []
        
        def dfs_topologico(v):
            visitados.add(v)
            for vecino in self._adyacencia[v]:
                if vecino not in visitados:
                    dfs_topologico(vecino)
            pila.append(v)  # agregar DESPUÉS de visitar todos los vecinos
        
        for v in self._adyacencia:
            if v not in visitados:
                dfs_topologico(v)
        
        return list(reversed(pila))
    
    # ------------------------------------------------------------------
    # Visualización
    # ------------------------------------------------------------------
    
    def __str__(self) -> str:
        tipo = "Dirigido" if self.dirigido else "No Dirigido"
        lineas = [f"Grafo {tipo} ({self.num_vertices()} vértices, {self.num_aristas()} aristas):"]
        for v in sorted(self._adyacencia, key=str):
            vecinos = sorted(self._adyacencia[v], key=str)
            flecha = "→" if self.dirigido else "—"
            lineas.append(f"  {v} {flecha} {vecinos}")
        return "\n".join(lineas)


# ------------------------------------------------------------------
# Demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Grafo No Dirigido ===")
    g = Grafo(dirigido=False)
    aristas = [('A','B'), ('A','C'), ('B','D'), ('B','E'), ('C','F'), ('D','E')]
    for u, v in aristas:
        g.agregar_arista(u, v)
    
    print(g)
    print(f"\nBFS desde A: {g.bfs('A')}")
    print(f"DFS desde A: {g.dfs('A')}")
    print(f"Camino más corto A→E: {g.camino_mas_corto('A', 'E')}")
    print(f"Camino más corto A→F: {g.camino_mas_corto('A', 'F')}")
    print(f"Grado de B: {g.grado('B')}")
    
    print("\n=== Grafo Dirigido (DAG) - Prerrequisitos ===")
    dag = Grafo(dirigido=True)
    prereqs = [
        ('Prog1', 'Prog2'), ('Prog1', 'Matematicas'),
        ('Prog2', 'ED1'), ('ED1', 'ED2'), ('Matematicas', 'ED2')
    ]
    for u, v in prereqs:
        dag.agregar_arista(u, v)
    
    print(dag)
    print(f"\nOrden topológico: {dag.orden_topologico()}")
    print(f"¿Tiene ciclo? {dag.tiene_ciclo()}")
    
    print("\n=== Grafo con ciclo ===")
    g_ciclo = Grafo(dirigido=True)
    for u, v in [('A','B'), ('B','C'), ('C','A')]:
        g_ciclo.agregar_arista(u, v)
    print(f"¿Tiene ciclo? {g_ciclo.tiene_ciclo()}")
    print(f"Orden topológico: {g_ciclo.orden_topologico()} (None porque tiene ciclo)")
