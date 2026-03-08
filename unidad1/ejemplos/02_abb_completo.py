# ejemplos/02_abb_completo.py
# Unidad I: Árbol Binario de Búsqueda (ABB) - Implementación Completa
# =====================================================================

class Nodo:
    """Nodo de un árbol binario."""
    
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
    
    def __repr__(self):
        return f"Nodo({self.dato})"


class ArbolBinarioBusqueda:
    """
    Implementación completa del Árbol Binario de Búsqueda (ABB).
    
    Propiedad ABB: para cada nodo N,
        - subárbol izquierdo < N.dato
        - subárbol derecho  > N.dato
    """
    
    def __init__(self):
        """Inicializa el árbol vacío."""
        self._raiz = None
        self._tamanio = 0
    
    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------
    
    def esta_vacio(self) -> bool:
        """Retorna True si el árbol no tiene nodos."""
        return self._raiz is None
    
    def __len__(self) -> int:
        return self._tamanio
    
    # ------------------------------------------------------------------
    # Inserción
    # ------------------------------------------------------------------
    
    def insertar(self, dato) -> None:
        """
        Inserta un nuevo dato manteniendo la propiedad ABB.
        Los valores duplicados son ignorados.
        
        Complejidad: O(h) donde h = altura del árbol.
        """
        self._raiz = self._insertar_rec(self._raiz, dato)
    
    def _insertar_rec(self, nodo: Nodo, dato) -> Nodo:
        """Auxiliar recursivo para insertar."""
        if nodo is None:
            self._tamanio += 1
            return Nodo(dato)
        
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._insertar_rec(nodo.derecho, dato)
        # dato == nodo.dato → duplicado, ignorar
        
        return nodo
    
    # ------------------------------------------------------------------
    # Búsqueda
    # ------------------------------------------------------------------
    
    def buscar(self, dato) -> bool:
        """
        Busca un dato en el árbol.
        
        Retorna:
            True si el dato existe, False en caso contrario.
        
        Complejidad: O(h)
        """
        return self._buscar_rec(self._raiz, dato)
    
    def _buscar_rec(self, nodo: Nodo, dato) -> bool:
        """Auxiliar recursivo para buscar."""
        if nodo is None:
            return False
        if dato == nodo.dato:
            return True
        if dato < nodo.dato:
            return self._buscar_rec(nodo.izquierdo, dato)
        return self._buscar_rec(nodo.derecho, dato)
    
    def obtener_nodo(self, dato) -> Nodo:
        """Retorna el nodo que contiene el dato, o None si no existe."""
        return self._obtener_nodo_rec(self._raiz, dato)
    
    def _obtener_nodo_rec(self, nodo: Nodo, dato) -> Nodo:
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._obtener_nodo_rec(nodo.izquierdo, dato)
        return self._obtener_nodo_rec(nodo.derecho, dato)
    
    # ------------------------------------------------------------------
    # Mínimo y Máximo
    # ------------------------------------------------------------------
    
    def minimo(self):
        """
        Retorna el valor mínimo del árbol.
        El mínimo siempre es el nodo más a la izquierda.
        """
        if self.esta_vacio():
            raise ValueError("El árbol está vacío")
        return self._minimo_nodo(self._raiz).dato
    
    def _minimo_nodo(self, nodo: Nodo) -> Nodo:
        """Retorna el nodo con el valor mínimo del subárbol."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    def maximo(self):
        """
        Retorna el valor máximo del árbol.
        El máximo siempre es el nodo más a la derecha.
        """
        if self.esta_vacio():
            raise ValueError("El árbol está vacío")
        nodo = self._raiz
        while nodo.derecho is not None:
            nodo = nodo.derecho
        return nodo.dato
    
    # ------------------------------------------------------------------
    # Eliminación
    # ------------------------------------------------------------------
    
    def eliminar(self, dato) -> bool:
        """
        Elimina un nodo con el dato dado.
        
        Casos:
            1. Nodo es hoja → eliminación directa.
            2. Nodo tiene 1 hijo → el padre apunta al hijo.
            3. Nodo tiene 2 hijos → reemplazar con sucesor inorden.
        
        Retorna:
            True si eliminó, False si el dato no existía.
        
        Complejidad: O(h)
        """
        if not self.buscar(dato):
            return False
        self._raiz = self._eliminar_rec(self._raiz, dato)
        self._tamanio -= 1
        return True
    
    def _eliminar_rec(self, nodo: Nodo, dato) -> Nodo:
        """Auxiliar recursivo para eliminar."""
        if nodo is None:
            return None
        
        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar_rec(nodo.derecho, dato)
        else:
            # ¡Nodo encontrado! Aplicar uno de los 3 casos:
            
            # Caso 1: Hoja (sin hijos)
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            
            # Caso 2a: Solo tiene hijo derecho
            if nodo.izquierdo is None:
                return nodo.derecho
            
            # Caso 2b: Solo tiene hijo izquierdo
            if nodo.derecho is None:
                return nodo.izquierdo
            
            # Caso 3: Tiene dos hijos
            # Encontrar el sucesor inorden (mínimo del subárbol derecho)
            sucesor = self._minimo_nodo(nodo.derecho)
            # Copiar el dato del sucesor al nodo actual
            nodo.dato = sucesor.dato
            # Eliminar el sucesor del subárbol derecho
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.dato)
        
        return nodo
    
    # ------------------------------------------------------------------
    # Información del árbol
    # ------------------------------------------------------------------
    
    def altura(self) -> int:
        """
        Calcula la altura del árbol.
        La altura de un árbol vacío es -1, la de un árbol con solo raíz es 0.
        """
        return self._altura_rec(self._raiz)
    
    def _altura_rec(self, nodo: Nodo) -> int:
        if nodo is None:
            return -1
        return 1 + max(self._altura_rec(nodo.izquierdo),
                       self._altura_rec(nodo.derecho))
    
    def es_balanceado(self) -> bool:
        """
        Verifica si el árbol está balanceado.
        Un árbol es balanceado si para cada nodo, la diferencia
        de altura entre sus subárboles es a lo sumo 1.
        """
        return self._es_balanceado_rec(self._raiz) != -2
    
    def _es_balanceado_rec(self, nodo: Nodo) -> int:
        """Retorna la altura o -2 si está desbalanceado."""
        if nodo is None:
            return -1
        alt_izq = self._es_balanceado_rec(nodo.izquierdo)
        if alt_izq == -2:
            return -2
        alt_der = self._es_balanceado_rec(nodo.derecho)
        if alt_der == -2:
            return -2
        if abs(alt_izq - alt_der) > 1:
            return -2
        return 1 + max(alt_izq, alt_der)
    
    # ------------------------------------------------------------------
    # Recorridos
    # ------------------------------------------------------------------
    
    def en_orden(self) -> list:
        """Recorrido en-orden: izq → raíz → der. Produce lista ordenada."""
        resultado = []
        self._en_orden_rec(self._raiz, resultado)
        return resultado
    
    def _en_orden_rec(self, nodo: Nodo, resultado: list) -> None:
        if nodo:
            self._en_orden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._en_orden_rec(nodo.derecho, resultado)
    
    def pre_orden(self) -> list:
        """Recorrido pre-orden: raíz → izq → der."""
        resultado = []
        self._pre_orden_rec(self._raiz, resultado)
        return resultado
    
    def _pre_orden_rec(self, nodo: Nodo, resultado: list) -> None:
        if nodo:
            resultado.append(nodo.dato)
            self._pre_orden_rec(nodo.izquierdo, resultado)
            self._pre_orden_rec(nodo.derecho, resultado)
    
    def post_orden(self) -> list:
        """Recorrido post-orden: izq → der → raíz."""
        resultado = []
        self._post_orden_rec(self._raiz, resultado)
        return resultado
    
    def _post_orden_rec(self, nodo: Nodo, resultado: list) -> None:
        if nodo:
            self._post_orden_rec(nodo.izquierdo, resultado)
            self._post_orden_rec(nodo.derecho, resultado)
            resultado.append(nodo.dato)
    
    def por_niveles(self) -> list:
        """Recorrido por niveles (BFS) usando una cola."""
        if self.esta_vacio():
            return []
        
        from collections import deque
        resultado = []
        cola = deque([self._raiz])
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        
        return resultado
    
    # ------------------------------------------------------------------
    # Visualización
    # ------------------------------------------------------------------
    
    def imprimir(self) -> None:
        """Imprime el árbol en formato visual (rotado 90°)."""
        self._imprimir_rec(self._raiz, 0)
    
    def _imprimir_rec(self, nodo: Nodo, nivel: int) -> None:
        if nodo:
            self._imprimir_rec(nodo.derecho, nivel + 1)
            print("    " * nivel + f"[{nodo.dato}]")
            self._imprimir_rec(nodo.izquierdo, nivel + 1)


# ------------------------------------------------------------------
# Demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    abb = ArbolBinarioBusqueda()
    
    valores = [50, 30, 70, 20, 40, 60, 80, 10, 35, 45]
    print("=== Árbol Binario de Búsqueda ===")
    print(f"Insertando: {valores}")
    for v in valores:
        abb.insertar(v)
    
    print(f"\nÁrbol (leer de abajo hacia arriba = de izq a der):")
    abb.imprimir()
    
    print(f"\nAltura: {abb.altura()}")
    print(f"Tamaño: {len(abb)}")
    print(f"Mínimo: {abb.minimo()}")
    print(f"Máximo: {abb.maximo()}")
    print(f"¿Balanceado? {abb.es_balanceado()}")
    
    print(f"\nRecorridos:")
    print(f"  En-orden   : {abb.en_orden()}")
    print(f"  Pre-orden  : {abb.pre_orden()}")
    print(f"  Post-orden : {abb.post_orden()}")
    print(f"  Por niveles: {abb.por_niveles()}")
    
    print(f"\n¿Existe 40? {abb.buscar(40)}")
    print(f"¿Existe 99? {abb.buscar(99)}")
    
    print(f"\nEliminando 30 (tiene 2 hijos)...")
    abb.eliminar(30)
    abb.imprimir()
    print(f"En-orden tras eliminar 30: {abb.en_orden()}")
