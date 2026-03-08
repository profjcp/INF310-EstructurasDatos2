# ejemplos/02_clases_abstractas.py
# Unidad 0: Interfaces con Clases Abstractas (ABC)
# =================================================
# En Python no existe la palabra "interface" como en Java,
# pero podemos simularla con el módulo 'abc'.

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# Interfaz (clase abstracta) para todas las estructuras de datos
# ---------------------------------------------------------------

class EstructuraDatos(ABC):
    """
    Clase abstracta que define el contrato (interfaz) para
    todas las estructuras de datos del curso.
    
    Cualquier clase que herede de esta DEBE implementar
    todos los métodos marcados con @abstractmethod.
    """
    
    @abstractmethod
    def insertar(self, dato) -> None:
        """Inserta un elemento en la estructura."""
        pass
    
    @abstractmethod
    def eliminar(self, dato) -> bool:
        """
        Elimina un elemento de la estructura.
        Retorna True si lo eliminó, False si no lo encontró.
        """
        pass
    
    @abstractmethod
    def buscar(self, dato) -> bool:
        """Busca un elemento. Retorna True si existe."""
        pass
    
    @abstractmethod
    def esta_vacia(self) -> bool:
        """Retorna True si la estructura no tiene elementos."""
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """Retorna la cantidad de elementos."""
        pass
    
    def __str__(self) -> str:
        """Representación por defecto (puede sobreescribirse)."""
        return f"{self.__class__.__name__}(elementos={len(self)})"


# ---------------------------------------------------------------
# Implementación concreta: Lista Simple
# ---------------------------------------------------------------

class ListaSimple(EstructuraDatos):
    """
    Implementación de lista enlazada simple.
    Usada como repaso de ED I.
    """
    
    class _Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
    
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0
    
    def insertar(self, dato) -> None:
        """Inserta al inicio de la lista."""
        nuevo = self._Nodo(dato)
        nuevo.siguiente = self._cabeza
        self._cabeza = nuevo
        self._tamanio += 1
    
    def eliminar(self, dato) -> bool:
        """Elimina la primera ocurrencia del dato."""
        anterior = None
        actual = self._cabeza
        
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self._cabeza = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        
        return False
    
    def buscar(self, dato) -> bool:
        """Busca un elemento en la lista."""
        actual = self._cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    def esta_vacia(self) -> bool:
        return self._tamanio == 0
    
    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        elementos = []
        actual = self._cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) + " -> None"


# ---------------------------------------------------------------
# Demo
# ---------------------------------------------------------------

if __name__ == "__main__":
    # Intentar instanciar la clase abstracta directo genera error:
    try:
        ed = EstructuraDatos()
    except TypeError as e:
        print(f"✗ No se puede instanciar clase abstracta: {e}\n")
    
    # La implementación concreta sí funciona:
    lista = ListaSimple()
    print("=== Demo de Clases Abstractas ===")
    print(f"Lista vacía: {lista.esta_vacia()}")
    
    for valor in [10, 20, 30, 40]:
        lista.insertar(valor)
    
    print(f"Después de insertar 10,20,30,40: {lista}")
    print(f"Tamaño: {len(lista)}")
    print(f"¿Existe 30? {lista.buscar(30)}")
    print(f"¿Existe 99? {lista.buscar(99)}")
    
    lista.eliminar(30)
    print(f"Después de eliminar 30: {lista}")
    
    # Polimorfismo: la función trabaja con cualquier EstructuraDatos
    def imprimir_info(estructura: EstructuraDatos):
        print(f"Tipo: {type(estructura).__name__}, "
              f"Vacía: {estructura.esta_vacia()}, "
              f"Tamaño: {len(estructura)}")
    
    print("\n=== Polimorfismo ===")
    imprimir_info(lista)
