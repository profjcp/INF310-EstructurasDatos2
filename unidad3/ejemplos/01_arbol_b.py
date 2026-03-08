# ejemplos/01_arbol_b.py
# Unidad III: Árbol-B - Inserción con Split
# ==========================================
# Implementación de un Árbol-B de orden m con inserción garantizando
# que todas las hojas queden al mismo nivel.

class NodoB:
    """
    Nodo de un Árbol-B.
    
    Atributos:
        claves (list): Claves almacenadas, siempre ordenadas.
        hijos (list): Punteros a los subárboles hijos.
        es_hoja (bool): True si el nodo no tiene hijos.
    """
    
    def __init__(self, es_hoja: bool = True):
        self.claves = []
        self.hijos = []
        self.es_hoja = es_hoja
    
    def __repr__(self):
        return f"NodoB({self.claves}, hoja={self.es_hoja})"


class ArbolB:
    """
    Árbol-B de orden m.
    
    Propiedades garantizadas:
    - Todas las hojas al mismo nivel (árbol perfectamente balanceado).
    - Cada nodo (excepto la raíz) tiene entre ⌈m/2⌉ y m hijos.
    - La raíz tiene entre 1 y m-1 claves.
    
    Complejidad de todas las operaciones: O(log n)
    """
    
    def __init__(self, orden: int):
        """
        Args:
            orden: Orden del árbol (m). Debe ser ≥ 2.
                   Con m=3 (árbol 2-3): máx 2 claves, mín 1 clave por nodo.
        """
        if orden < 2:
            raise ValueError("El orden debe ser al menos 2")
        self.orden = orden
        self.t = (orden + 1) // 2  # grado mínimo t = ⌈m/2⌉
        self._raiz = NodoB(es_hoja=True)
    
    # ------------------------------------------------------------------
    # Búsqueda
    # ------------------------------------------------------------------
    
    def buscar(self, clave) -> bool:
        """Busca una clave en el árbol. O(log n)."""
        return self._buscar_rec(self._raiz, clave)
    
    def _buscar_rec(self, nodo: NodoB, clave) -> bool:
        # Encontrar la primera clave >= clave
        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1
        
        if i < len(nodo.claves) and nodo.claves[i] == clave:
            return True  # encontrada
        
        if nodo.es_hoja:
            return False  # no existe
        
        return self._buscar_rec(nodo.hijos[i], clave)
    
    # ------------------------------------------------------------------
    # Inserción
    # ------------------------------------------------------------------
    
    def insertar(self, clave) -> None:
        """
        Inserta una clave manteniendo todas las propiedades del Árbol-B.
        Si la raíz se desborda, se hace split y el árbol crece hacia arriba.
        
        O(log n)
        """
        raiz = self._raiz
        
        # Si la raíz está llena, hacer split ANTES de insertar
        if len(raiz.claves) == self.orden - 1:
            nueva_raiz = NodoB(es_hoja=False)
            nueva_raiz.hijos.append(self._raiz)
            self._split_hijo(nueva_raiz, 0)
            self._raiz = nueva_raiz
        
        self._insertar_no_lleno(self._raiz, clave)
    
    def _insertar_no_lleno(self, nodo: NodoB, clave) -> None:
        """Inserta en un nodo que garantizadamente NO está lleno."""
        i = len(nodo.claves) - 1
        
        if nodo.es_hoja:
            # Insertar la clave en la posición correcta
            nodo.claves.append(None)  # espacio temporal
            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = clave
        else:
            # Encontrar el hijo correcto
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1
            i += 1
            
            # Si el hijo está lleno, hacer split primero
            if len(nodo.hijos[i].claves) == self.orden - 1:
                self._split_hijo(nodo, i)
                # Después del split, decidir en cuál de los dos hijos insertar
                if clave > nodo.claves[i]:
                    i += 1
            
            self._insertar_no_lleno(nodo.hijos[i], clave)
    
    def _split_hijo(self, padre: NodoB, i: int) -> None:
        """
        Divide el hijo i-ésimo del padre (que está lleno).
        
        Pasos:
        1. Crear nuevo nodo con la mitad derecha de las claves.
        2. Promover la clave del medio al padre.
        3. El hijo original retiene la mitad izquierda.
        """
        t = self.t
        hijo_lleno = padre.hijos[i]
        nuevo_nodo = NodoB(es_hoja=hijo_lleno.es_hoja)
        
        # La clave del medio (índice t-1) sube al padre
        clave_media = hijo_lleno.claves[t - 1]
        
        # El nuevo nodo recibe la mitad derecha de las claves
        nuevo_nodo.claves = hijo_lleno.claves[t:]
        
        # Si no es hoja, también dividir los hijos
        if not hijo_lleno.es_hoja:
            nuevo_nodo.hijos = hijo_lleno.hijos[t:]
            hijo_lleno.hijos = hijo_lleno.hijos[:t]
        
        # El hijo original retiene solo la mitad izquierda
        hijo_lleno.claves = hijo_lleno.claves[:t - 1]
        
        # Insertar la clave media en el padre
        padre.claves.insert(i, clave_media)
        
        # Insertar el nuevo nodo en los hijos del padre
        padre.hijos.insert(i + 1, nuevo_nodo)
    
    # ------------------------------------------------------------------
    # Recorridos
    # ------------------------------------------------------------------
    
    def en_orden(self) -> list:
        """Recorrido en-orden. Produce lista ordenada."""
        resultado = []
        self._en_orden_rec(self._raiz, resultado)
        return resultado
    
    def _en_orden_rec(self, nodo: NodoB, resultado: list) -> None:
        if nodo is None:
            return
        for i in range(len(nodo.claves)):
            if not nodo.es_hoja:
                self._en_orden_rec(nodo.hijos[i], resultado)
            resultado.append(nodo.claves[i])
        if not nodo.es_hoja:
            self._en_orden_rec(nodo.hijos[-1], resultado)
    
    # ------------------------------------------------------------------
    # Información y visualización
    # ------------------------------------------------------------------
    
    def altura(self) -> int:
        """Calcula la altura del árbol (todas las hojas al mismo nivel)."""
        h = 0
        nodo = self._raiz
        while not nodo.es_hoja:
            h += 1
            nodo = nodo.hijos[0]
        return h
    
    def imprimir(self) -> None:
        """Imprime el árbol nivel por nivel."""
        from collections import deque
        cola = deque([(self._raiz, 0)])
        nivel_actual = -1
        
        while cola:
            nodo, nivel = cola.popleft()
            
            if nivel != nivel_actual:
                print(f"\nNivel {nivel}:", end=" ")
                nivel_actual = nivel
            
            print(nodo.claves, end="  ")
            
            if not nodo.es_hoja:
                for hijo in nodo.hijos:
                    cola.append((hijo, nivel + 1))
        print()


# ------------------------------------------------------------------
# Demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Árbol-B de orden 5 ===")
    print("(máx 4 claves por nodo, mín 2 claves en no-raíz)\n")
    
    arbol = ArbolB(orden=5)
    
    valores = [3, 7, 1, 14, 5, 11, 17, 13, 6, 23, 12, 20, 26, 4, 16, 18, 24, 25, 19]
    
    print(f"Insertando: {valores}\n")
    for v in valores:
        arbol.insertar(v)
    
    print("Árbol por niveles:")
    arbol.imprimir()
    
    print(f"\nAltura del árbol: {arbol.altura()}")
    print(f"En-orden (debe ser ordenado): {arbol.en_orden()}")
    
    print(f"\nBúsquedas:")
    for clave in [14, 25, 99, 3]:
        print(f"  ¿Existe {clave}? {arbol.buscar(clave)}")
    
    print("\n=== Árbol-B de orden 3 (árbol 2-3) ===")
    arbol3 = ArbolB(orden=3)
    for v in [10, 20, 5, 6, 12, 30, 7, 17]:
        arbol3.insertar(v)
        
    print("Árbol por niveles:")
    arbol3.imprimir()
    print(f"En-orden: {arbol3.en_orden()}")
    print(f"Altura: {arbol3.altura()}")
