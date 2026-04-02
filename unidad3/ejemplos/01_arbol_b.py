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
        if self.buscar(clave):
            return  # ignorar duplicados

        promocion = self._insertar_rec(self._raiz, clave)

        # Si la raíz se desbordó, crear nueva raíz y subir la clave media.
        if promocion is not None:
            clave_media, nuevo_derecho = promocion
            nueva_raiz = NodoB(es_hoja=False)
            nueva_raiz.claves = [clave_media]
            nueva_raiz.hijos = [self._raiz, nuevo_derecho]
            self._raiz = nueva_raiz

    def _insertar_rec(self, nodo: NodoB, clave):
        """
        Inserta recursivamente y retorna una promoción opcional.

        Retorna:
            None, si no hubo desborde
            (clave_media, nuevo_nodo_derecho), si hubo split del nodo actual
        """
        if nodo.es_hoja:
            i = 0
            while i < len(nodo.claves) and clave > nodo.claves[i]:
                i += 1
            nodo.claves.insert(i, clave)
        else:
            i = 0
            while i < len(nodo.claves) and clave > nodo.claves[i]:
                i += 1

            promocion_hijo = self._insertar_rec(nodo.hijos[i], clave)
            if promocion_hijo is not None:
                clave_media, nuevo_hijo_derecho = promocion_hijo
                nodo.claves.insert(i, clave_media)
                nodo.hijos.insert(i + 1, nuevo_hijo_derecho)

        if len(nodo.claves) > self.orden - 1:
            return self._dividir_nodo(nodo)

        return None

    def _dividir_nodo(self, nodo: NodoB):
        """
        Divide un nodo desbordado (len(claves) == orden) y retorna
        la clave promovida junto al nuevo nodo derecho.
        """
        medio = len(nodo.claves) // 2
        clave_media = nodo.claves[medio]

        derecho = NodoB(es_hoja=nodo.es_hoja)
        derecho.claves = nodo.claves[medio + 1:]
        nodo.claves = nodo.claves[:medio]

        if not nodo.es_hoja:
            derecho.hijos = nodo.hijos[medio + 1:]
            nodo.hijos = nodo.hijos[:medio + 1]

        return clave_media, derecho
    
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
