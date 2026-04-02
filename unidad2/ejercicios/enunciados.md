# Unidad II · Ejercicios: Árboles M-Vías

## Ejercicio 1 — Comprensión del modelo [Básico]

Dado un árbol M-Vías de **orden 4**:

```
              [20, 40, 60]
             /    |    |    \
         [10]  [30]  [50]  [70, 80]
```

a) ¿Cuántas claves tiene la raíz? ¿Se respeta la restricción del orden 4?  
b) ¿Cuántos hijos tiene la raíz? ¿Es correcto para orden 4?  
c) ¿Cuál es la clave inmediatamente anterior a 50 en el árbol? ¿Y la posterior?  
d) Para un árbol M-Vías de orden `m`, ¿cuántas claves como máximo puede tener un nodo? ¿Y cuántos hijos?

---

## Ejercicio 2 — Búsqueda manual [Básico]

Usando el árbol del Ejercicio 1, indica el **camino de búsqueda** (secuencia de nodos visitados) para:

a) Buscar la clave **50** (debe encontrarse).  
b) Buscar la clave **25** (no existe).  
c) Buscar la clave **80** (debe encontrarse).  

Para cada búsqueda, indica en qué índice dentro del nodo se encontró (o no) la clave.

---

## Ejercicio 3 — Inserción manual [Intermedio]

Dado un árbol M-Vías vacío de **orden 3**, inserta las siguientes claves en orden:

**5, 10, 3, 7, 15, 1, 9, 12, 20, 6**

> Recordatorio: en un árbol M-Vías (sin balanceo), la inserción se realiza en el nodo hoja adecuado según la clave, siempre que el nodo tenga espacio.

a) Dibuja el árbol después de cada inserción.  
b) ¿Qué ocurre cuando un nodo llega a tener `m-1 = 2` claves? ¿Puede seguir recibiendo claves?  
c) ¿Qué diferencia hay con un Árbol-B en este punto?

---

## Ejercicio 4 — Recorrido [Intermedio]

Para el árbol del Ejercicio 1, realiza el **recorrido en-orden** (inorden generalizado para M-vías):

> Para un nodo con claves [k₁, k₂, ..., kₙ] e hijos [h₀, h₁, ..., hₙ]:
> Recorrer h₀, luego k₁, luego h₁, luego k₂, ..., luego hₙ₋₁, luego kₙ, luego hₙ.

a) Escribe la secuencia de claves resultante del recorrido en-orden.  
b) ¿Está ordenada? ¿Por qué?  
c) ¿Cuál sería el resultado del recorrido **pre-orden**?

---

## Ejercicio 5 — Implementación: recorrido en-orden [Intermedio]

Agrega el siguiente método a la clase `ArbolMVias`:

```python
def recorrido_enorden(self) -> list:
    """
    Retorna una lista con todas las claves del árbol en orden ascendente,
    usando el recorrido en-orden generalizado para M-vías.
    """
    pass
```

Verifica que para el árbol `[20,40,60] / [10] [30] [50] [70,80]` el resultado sea:
`[10, 20, 30, 40, 50, 60, 70, 80]`

---

## Ejercicio 6 — Comparación con ABB [Desafío]

a) Para almacenar **n = 1000** claves en un ABB balanceado (altura ≈ log₂ n),
   ¿cuántas comparaciones se necesitan en el peor caso para una búsqueda?  
b) Para el mismo conjunto en un árbol M-Vías de orden **m = 10** balanceado
   (altura ≈ log₁₀ n), ¿cuántos nodos se visitan?  
c) ¿En qué escenario real preferiríamos un árbol M-Vías de orden alto sobre un ABB?  
   (Pista: pensar en acceso a disco vs. acceso a RAM.)

---

## 📋 Rúbrica de evaluación

| Criterio | Puntos |
|----------|--------|
| Código funciona correctamente | 40% |
| Código bien documentado (docstrings) | 20% |
| Manejo de casos borde (árbol vacío, clave no encontrada) | 20% |
| Nombres descriptivos y buenas prácticas | 20% |
