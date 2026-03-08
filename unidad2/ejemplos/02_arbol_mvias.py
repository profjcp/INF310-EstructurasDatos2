# ejemplos/02_arbol_mvias.py
# Unidad II: Árbol M-Vías - Implementación en Python
# ====================================================

class NodoMVias:
    """
    Nodo de un árbol m-vías.
    
    Atributos:
        orden (int): Número máximo de hijos (m).
        claves (list): Lista de hasta m-1 claves ordenadas.
        hijos (list): Lista de hasta m punteros a subárboles.
    """
    
    def __init__(self, orden: int):
        self.orden = orden          # m
        self.claves = []            # hasta m-1 claves
        self.hijos = []             # hasta m punteros
    
    def es_hoja(self) -> bool:
        """Retorna True si el nodo no tiene hijos."""
        return all(h is None for h in self.hijos) or len(self.hijos) == 0
    
    def esta_lleno(self) -> bool:
        """Retorna True si el nodo tiene m-1 claves (máximo permitido)."""
        return len(self.claves) >= self.orden - 1
    
    def __repr__(self) -> str:
        return f"NodoMVias(claves={self.claves})"


class ArbolMVias:
    """
    Árbol M-Vías de orden m.
    
    Cada nodo puede almacenar hasta m-1 claves y tener hasta m hijos.
    Para m=2 se comporta como un ABB.
    
    Nota: Esta implementación no controla el balanceo.
    Para árboles balanceados ver Unidad III (Árboles-B).
    """
    
    def __init__(self, orden: int):
        """
        Inicializa el árbol de orden m.
        
        Args:
            orden: Número máximo de hijos por nodo (m >= 2).
        """
        if orden < 2:
            raise ValueError("El orden debe ser al menos 2")
        self.orden = orden
        self._raiz = None
    
    def esta_vacio(self) -> bool:
        return self._raiz is None
    
    # ------------------------------------------------------------------
    # Búsqueda
    # ------------------------------------------------------------------
    
    def buscar(self, clave) -> bool:
        """
        Busca una clave en el árbol.
        
        Complejidad: O(m × log_m(n))
        
        Retorna:
            True si la clave existe, False en caso contrario.
        """
        return self._buscar_rec(self._raiz, clave)
    
    def _buscar_rec(self, nodo: NodoMVias, clave) -> bool:
        """Auxiliar recursivo para buscar."""
        if nodo is None:
            return False
        
        # Buscar la clave en el nodo actual
        for i, k in enumerate(nodo.claves):
            if clave == k:
                return True          # ¡encontrada!
            if clave < k:
                # La clave debería estar en el subárbol i (a la izquierda de k)
                if i < len(nodo.hijos):
                    return self._buscar_rec(nodo.hijos[i], clave)
                return False
        
        # La clave es mayor que todas las claves del nodo
        if len(nodo.hijos) > len(nodo.claves):
            return self._buscar_rec(nodo.hijos[-1], clave)
        return False
    
    # ------------------------------------------------------------------
    # Inserción (sin balanceo)
    # ------------------------------------------------------------------
    
    def insertar(self, clave) -> None:
        """
        Inserta una clave en el árbol.
        
        Si el árbol está vacío, crea la raíz.
        Si la hoja tiene espacio, inserta directamente.
        
        Nota: Esta versión no hace split. Ver Árbol-B para inserción balanceada.
        """
        if self._raiz is None:
            self._raiz = NodoMVias(self.orden)
            self._raiz.claves.append(clave)
            return
        
        self._insertar_rec(self._raiz, clave)
    
    def _insertar_rec(self, nodo: NodoMVias, clave) -> None:
        """Auxiliar recursivo para insertar (sin split)."""
        # Si es hoja, insertar aquí (si hay espacio)
        if nodo.es_hoja():
            if not nodo.esta_lleno():
                self._insertar_ordenado(nodo.claves, clave)
            # Si está lleno: en árbol-B haríamos split, aquí lo saltamos
            return
        
        # No es hoja: encontrar el hijo correcto
        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1
        
        if i < len(nodo.hijos) and nodo.hijos[i] is not None:
            self._insertar_rec(nodo.hijos[i], clave)
        else:
            # Crear nuevo hijo hoja
            nuevo = NodoMVias(self.orden)
            nuevo.claves.append(clave)
            while len(nodo.hijos) <= i:
                nodo.hijos.append(None)
            nodo.hijos[i] = nuevo
    
    def _insertar_ordenado(self, lista: list, valor) -> None:
        """Inserta un valor manteniendo la lista ordenada."""
        i = 0
        while i < len(lista) and valor > lista[i]:
            i += 1
        lista.insert(i, valor)
    
    # ------------------------------------------------------------------
    # Recorridos
    # ------------------------------------------------------------------
    
    def en_orden(self) -> list:
        """
        Recorrido en-orden generalizado.
        Para un ABB produce lista ordenada; aquí también.
        """
        resultado = []
        self._en_orden_rec(self._raiz, resultado)
        return resultado
    
    def _en_orden_rec(self, nodo: NodoMVias, resultado: list) -> None:
        if nodo is None:
            return
        
        num_claves = len(nodo.claves)
        
        for i in range(num_claves):
            # Visitar subárbol i (a la izquierda de la clave i)
            if i < len(nodo.hijos):
                self._en_orden_rec(nodo.hijos[i], resultado)
            # Visitar clave i
            resultado.append(nodo.claves[i])
        
        # Visitar el último subárbol (a la derecha de todas las claves)
        if len(nodo.hijos) > num_claves:
            self._en_orden_rec(nodo.hijos[num_claves], resultado)
    
    def por_niveles(self) -> list:
        """Recorrido por niveles (BFS)."""
        if self.esta_vacio():
            return []
        
        from collections import deque
        resultado = []
        cola = deque([self._raiz])
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.claves[:])  # copia de las claves del nodo
            for hijo in nodo.hijos:
                if hijo is not None:
                    cola.append(hijo)
        
        return resultado
    
    # ------------------------------------------------------------------
    # Visualización
    # ------------------------------------------------------------------
    
    def imprimir(self) -> None:
        """Imprime el árbol nivel por nivel."""
        if self.esta_vacio():
            print("(árbol vacío)")
            return
        
        from collections import deque
        cola = deque([(self._raiz, 0)])
        nivel_actual = 0
        linea = []
        
        while cola:
            nodo, nivel = cola.popleft()
            
            if nivel != nivel_actual:
                print(f"Nivel {nivel_actual}: " + "  |  ".join(str(c) for c in linea))
                linea = []
                nivel_actual = nivel
            
            linea.append(nodo.claves)
            
            for hijo in nodo.hijos:
                if hijo is not None:
                    cola.append((hijo, nivel + 1))
        
        if linea:
            print(f"Nivel {nivel_actual}: " + "  |  ".join(str(c) for c in linea))


# ------------------------------------------------------------------
# Demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Árbol M-Vías de orden 4 ===")
    print("(cada nodo puede tener hasta 3 claves y 4 hijos)\n")
    
    arbol = ArbolMVias(orden=4)
    
    valores = [50, 25, 75, 10, 30, 60, 90, 5, 15, 27, 35]
    print(f"Insertando: {valores}")
    for v in valores:
        arbol.insertar(v)
    
    print("\nEstructura por niveles:")
    arbol.imprimir()
    
    print(f"\nRecorrido en-orden: {arbol.en_orden()}")
    
    print(f"\n¿Existe 30? {arbol.buscar(30)}")
    print(f"¿Existe 99? {arbol.buscar(99)}")
    
    print("\n=== Comparación de alturas según orden ===")
    import math
    n = 1_000_000
    for m in [2, 10, 50, 100, 500]:
        altura = math.ceil(math.log(n, m))
        print(f"  Orden {m:4d}: altura ≈ {altura} (log_{m}({n:,})) → {altura} accesos a disco")
