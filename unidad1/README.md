# Unidad I · Árboles Binarios de Búsqueda (ABB)

**Tiempo estimado:** 24 horas

## 🎯 Objetivo

Aplicar el ADT Árbol Binario a diversos problemas de búsqueda de datos, comprendiendo su estructura, operaciones y recorridos.

---

## 1. Conceptos Generales

### ¿Qué es un árbol?

Un **árbol** es una estructura de datos jerárquica no lineal formada por nodos conectados mediante aristas. A diferencia de las listas, un nodo puede tener más de un "siguiente".

```
Ejemplo de árbol binario:

        50          ← Raíz (nivel 0)
       /  \
     30    70       ← Nivel 1
    /  \     \
   20  40    80     ← Nivel 2 (hojas)
```

### Terminología clave

| Término | Definición |
|---------|-----------|
| **Raíz** | Nodo sin padre. Único punto de entrada al árbol. |
| **Hoja** | Nodo sin hijos. |
| **Padre/Hijo** | Relación entre nodo y sus subnodos. |
| **Subárbol** | Un nodo y todos sus descendientes. |
| **Altura** | Número de aristas en el camino más largo desde la raíz a una hoja. |
| **Profundidad** | Número de aristas desde la raíz hasta un nodo específico. |
| **Nivel** | Profundidad del nodo (raíz = nivel 0). |

### ¿Qué es un Árbol Binario?

Un **árbol binario** es un árbol donde cada nodo tiene **a lo sumo 2 hijos**: el hijo **izquierdo** y el hijo **derecho**.

### ¿Qué es un Árbol Binario de Búsqueda (ABB)?

Un ABB es un árbol binario con una propiedad especial llamada **propiedad de ordenamiento**:

> Para cualquier nodo `N`:
> - Todos los valores en el **subárbol izquierdo** son **menores** que `N.dato`
> - Todos los valores en el **subárbol derecho** son **mayores** que `N.dato`

```
ABB con valores: 50, 30, 70, 20, 40, 60, 80

        50
       /  \
     30    70
    /  \  /  \
   20  40 60  80
   
✓ 20 < 30 < 40 (subárbol izquierdo de 30)
✓ 60 < 70 < 80 (subárbol derecho de 70)
✓ Todo el subárbol izq (20,30,40) < 50 < subárbol der (60,70,80)
```

---

## 2. El ADT Árbol Binario

El **Tipo de Dato Abstracto (ADT)** Árbol Binario define:

### Operaciones básicas

| Operación | Descripción |
|-----------|-------------|
| `insertar(dato)` | Agrega un nuevo nodo manteniendo la propiedad ABB |
| `eliminar(dato)` | Elimina un nodo (3 casos posibles) |
| `buscar(dato)` | Busca un valor, retorna True/False |
| `esta_vacio()` | Verifica si el árbol no tiene nodos |
| `raiz()` | Retorna el dato de la raíz |

### Operaciones de consulta

| Operación | Descripción |
|-----------|-------------|
| `altura()` | Calcula la altura del árbol |
| `contar_nodos()` | Cuenta el total de nodos |
| `minimo()` | Retorna el valor mínimo (nodo más a la izquierda) |
| `maximo()` | Retorna el valor máximo (nodo más a la derecha) |

---

## 3. Operaciones sobre Árboles

### 3.1 Inserción

La inserción sigue la propiedad ABB:

```
Insertar 45 en el árbol:

        50
       /  \
     30    70
    /  \
   20  40
        \
        45   ← ¡nuevo nodo!

Pasos:
1. ¿45 < 50? → ir a la izquierda (30)
2. ¿45 > 30? → ir a la derecha (40)
3. ¿45 > 40? → ir a la derecha → NULL → insertar aquí
```

**Algoritmo recursivo:**
```python
def _insertar_rec(self, nodo, dato):
    if nodo is None:
        return Nodo(dato)          # caso base: lugar encontrado
    if dato < nodo.dato:
        nodo.izquierdo = self._insertar_rec(nodo.izquierdo, dato)
    elif dato > nodo.dato:
        nodo.derecho = self._insertar_rec(nodo.derecho, dato)
    # Si dato == nodo.dato: ignorar (no se permiten duplicados)
    return nodo
```

**Complejidad:** O(h) donde h es la altura del árbol. En un árbol balanceado: O(log n).

---

### 3.2 Búsqueda

```
Buscar 40:
1. ¿40 == 50? No. ¿40 < 50? Sí → izquierda (30)
2. ¿40 == 30? No. ¿40 > 30? Sí → derecha (40)
3. ¿40 == 40? ✓ ENCONTRADO
```

**Complejidad:** O(h) → O(log n) en árbol balanceado.

---

### 3.3 Eliminación (3 casos)

**Caso 1: El nodo es una hoja** → simplemente se elimina.

```
Eliminar 20:
     30          30
    /  \    →      \
   20  40          40
```

**Caso 2: El nodo tiene UN hijo** → el padre apunta al hijo del nodo eliminado.

```
Eliminar 70 (tiene solo hijo derecho 80):
     50          50
    /  \    →   /  \
   30  70       30  80
         \
         80
```

**Caso 3: El nodo tiene DOS hijos** → reemplazar con el **sucesor inorden** (mínimo del subárbol derecho) o el **predecesor** (máximo del subárbol izquierdo).

```
Eliminar 30 (tiene hijos 20 y 40):
     50               50
    /  \    →         /  \
   30  70    sucesor=40  70
  /  \              /
 20  40            20
```

---

## 4. Recorridos en Árboles Binarios

Un **recorrido** visita todos los nodos del árbol exactamente una vez. Hay tres recorridos clásicos (todos recursivos):

### 4.1 En-Orden (Inorder): izq → raíz → der

> ⭐ En un ABB, el recorrido en-orden produce los valores **ordenados de menor a mayor**.

```
        50
       /  \
     30    70
    /  \
   20  40

En-orden: 20, 30, 40, 50, 70
```

### 4.2 Pre-Orden (Preorder): raíz → izq → der

> Útil para **copiar** o **serializar** el árbol.

```
Pre-orden: 50, 30, 20, 40, 70
```

### 4.3 Post-Orden (Postorder): izq → der → raíz

> Útil para **eliminar** el árbol o calcular expresiones.

```
Post-orden: 20, 40, 30, 70, 50
```

### 4.4 Recorrido por Niveles (BFS)

Visita los nodos nivel por nivel, de izquierda a derecha. Usa una **cola**.

```
Por niveles: 50, 30, 70, 20, 40
```

---

## 5. Aplicaciones

Los ABB se usan en situaciones reales donde necesitamos búsqueda eficiente:

- **Diccionarios y mapas**: encontrar rápidamente un valor dado su clave.
- **Bases de datos**: índices de tablas para búsquedas rápidas.
- **Autocompletado**: buscar palabras que empiecen con un prefijo.
- **Ranking y clasificación**: mantener un conjunto ordenado dinámico.
- **Expresiones matemáticas**: los compiladores representan expresiones como árboles.

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_nodo_arbol.py`](./ejemplos/01_nodo_arbol.py) | Clase Nodo básica |
| [`ejemplos/02_abb_completo.py`](./ejemplos/02_abb_completo.py) | ABB con todas las operaciones |
| [`ejemplos/03_recorridos.py`](./ejemplos/03_recorridos.py) | Los 4 recorridos |
| [`ejemplos/04_aplicacion_agenda.py`](./ejemplos/04_aplicacion_agenda.py) | Aplicación práctica |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
