# unidad1/ejercicios/plantilla_ej07_agenda.py
# Ejercicio 7 — Agenda Telefónica con ABB
# =====================================================================
# INSTRUCCIONES:
#   1. Implementa las clases Contacto y AgendaTelefonica abajo.
#   2. Ejecuta: python plantilla_ej07_agenda.py
#   3. Si todos los asserts pasan verás "✓ Todos los tests pasaron."
#
# La clave de ordenamiento del ABB es el nombre del contacto.
# =====================================================================

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


class Contacto:
    """Representa un contacto con nombre (clave) y teléfono."""

    def __init__(self, nombre: str, telefono: str):
        # TODO: guarda los atributos
        raise NotImplementedError


class AgendaTelefonica:
    """
    Agenda telefónica implementada internamente con un ABB.
    La clave de ordenamiento es el nombre del contacto.
    """

    def agregar(self, nombre: str, telefono: str) -> None:
        """Agrega o actualiza un contacto."""
        raise NotImplementedError

    def buscar(self, nombre: str) -> str | None:
        """
        Retorna el teléfono del contacto con ese nombre.
        Retorna None si no existe.
        """
        raise NotImplementedError

    def eliminar(self, nombre: str) -> bool:
        """
        Elimina el contacto con ese nombre.
        Retorna True si existía, False si no.
        """
        raise NotImplementedError

    def listar_alfabetico(self) -> list[tuple[str, str]]:
        """
        Retorna una lista de tuplas (nombre, telefono) ordenada
        alfabéticamente. Usa recorrido en-orden del ABB.
        """
        raise NotImplementedError


# ------------------------------------------------------------------
# Tests automáticos
# ------------------------------------------------------------------
agenda = AgendaTelefonica()

agenda.agregar("Maria", "+591-70012345")
agenda.agregar("Carlos", "+591-71123456")
agenda.agregar("Ana", "+591-72234567")
agenda.agregar("Pedro", "+591-73345678")
agenda.agregar("Lucia", "+591-74456789")

# Búsqueda
assert agenda.buscar("Ana") == "+591-72234567", "Teléfono de Ana incorrecto"
assert agenda.buscar("Carlos") == "+591-71123456", "Teléfono de Carlos incorrecto"
assert agenda.buscar("Zara") is None, "Contacto inexistente debe retornar None"

# Listado ordenado
lista = agenda.listar_alfabetico()
nombres = [nombre for nombre, _ in lista]
assert nombres == sorted(nombres), f"La lista no está ordenada: {nombres}"
assert len(lista) == 5, f"Se esperaban 5 contactos, hay {len(lista)}"

# Eliminación
assert agenda.eliminar("Carlos") is True, "Debería eliminar a Carlos"
assert agenda.buscar("Carlos") is None, "Carlos ya no debe existir"
assert agenda.eliminar("Inexistente") is False, "Eliminar inexistente debe retornar False"
assert len(agenda.listar_alfabetico()) == 4, "Deben quedar 4 contactos"

# Actualizar teléfono
agenda.agregar("Ana", "+591-99000000")
assert agenda.buscar("Ana") == "+591-99000000", "El teléfono de Ana debería estar actualizado"

print("✓ Todos los tests pasaron.")
