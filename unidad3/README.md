# Unidad III · Árboles-B

**Tiempo estimado:** 24 horas

## 🎯 Objetivo

Resolver el problema del desbalance que se presenta en los árboles m-vías, garantizando eficiencia incluso en el peor caso.

---

## 1. El Problema del Desbalance

### 1.1 El desbalance en los árboles binarios

Los ABB pueden degenerarse si insertamos datos en orden:

```
Insertar: 10, 20, 30, 40, 50 (en orden ascendente)

10
  \
  20
    \
    30
      \
      40
        \
        50

¡Se convierte en una lista! Altura = n-1 = 4 → búsqueda O(n)
```

### 1.2 El desbalance en los árboles m-vías

El mismo problema ocurre en árboles m-vías. Si no controlamos cómo crecen, algunos subárboles se hacen mucho más profundos que otros.

**Consecuencia:** Las búsquedas en una rama profunda son mucho más lentas → no sirve para bases de datos donde se requiere **garantía de tiempo constante**.

---

## 2. El Árbol-B: Solución al Desbalance

Un **Árbol-B de orden m** es un árbol m-vía que además cumple estas reglas estrictas:

### Propiedades del Árbol-B

| # | Propiedad |
|---|-----------|
| 1 | La raíz tiene entre **1 y m-1** claves (y entre 2 y m hijos, si no es hoja). |
| 2 | Todos los nodos **no-raíz** tienen entre **⌈m/2⌉-1 y m-1** claves. |
| 3 | Todos los nodos **no-raíz** tienen entre **⌈m/2⌉ y m** hijos. |
| 4 | **Todas las hojas están en el mismo nivel** (árbol perfectamente balanceado). |
| 5 | Las claves dentro de cada nodo están **ordenadas**. |

> La propiedad 4 es la clave: **garantiza O(log n)** para todas las operaciones.

### Ejemplo: Árbol-B de orden 5

```
Orden m=5:
  - Máximo de claves por nodo: 4 (m-1)
  - Mínimo de claves por nodo (no raíz): 2 (⌈5/2⌉-1)
  - Máximo de hijos: 5 (m)
  - Mínimo de hijos (no hoja): 3 (⌈5/2⌉)

                    [30 | 70]
                   /    |    \
         [10|20]    [40|50|60]    [80|90]
        /  |  \    /  |  |  \    /  |  \
       ...      ...              ...
       
¡Todas las hojas están al mismo nivel!
```

---

## 3. Inserción en un Árbol-B

La inserción siempre ocurre en una hoja. Si la hoja se desborda, se produce un **split (división)**.

### Algoritmo de inserción

```
1. Buscar la hoja correcta (igual que en árbol m-vías).
2. Insertar la clave en la hoja.
3. Si la hoja tiene ≤ m-1 claves → FIN.
4. Si la hoja tiene m claves → SPLIT:
   a. Dividir el nodo en dos nodos de ⌊m/2⌋ claves cada uno.
   b. Promover la clave del medio al nodo padre.
   c. Si el padre también se desborda → hacer split del padre.
   d. Si la raíz se desborda → crear nueva raíz (el árbol crece hacia arriba).
```

### Ejemplo: Insertar en Árbol-B de orden 3

```
Orden 3: máx 2 claves, mín 1 clave (para no-raíz)

Estado inicial:
    [10 | 20]

Insertar 30 → hoja se desborda (tiene 3 claves: 10,20,30)
→ SPLIT: promover 20

       [20]
      /    \
   [10]    [30]

Insertar 40 → va a la hoja [30]:
       [20]
      /    \
   [10]    [30|40]

Insertar 50 → hoja [30|40|50] se desborda → SPLIT, promover 40

       [20 | 40]
      /    |    \
   [10]  [30]  [50]
```

---

## 4. Eliminación en un Árbol-B

La eliminación es más compleja que la inserción.

### Caso A: Eliminar de una hoja

1. Eliminar la clave directamente.
2. Si el nodo queda con ≥ ⌈m/2⌉-1 claves → FIN.
3. Si el nodo queda **deficiente** (menos del mínimo):
   - **Préstamo:** Si un hermano tiene claves extra, rotar a través del padre.
   - **Fusión:** Si ningún hermano tiene extra, fusionar con un hermano + bajar clave del padre.

### Caso B: Eliminar de un nodo interno

Reemplazar la clave con su **sucesor inorden** (mínimo del subárbol derecho) o **predecesor** (máximo del subárbol izquierdo), que siempre está en una hoja. Luego eliminar de la hoja (caso A).

### Ejemplo de préstamo (rotación)

```
Árbol-B orden 5 (mín 2 claves):

       [30 | 60]
      /    |    \
 [10|20]  [40|50]  [70|80|90]   ← hermano derecho tiene 3 claves (extra)

Eliminar 40 de [40|50]:
  [50] → deficiente (solo 1 clave, mínimo es 2)
  
→ Préstamo del hermano derecho [70|80|90]:
  1. Rotar: 60 baja al nodo deficiente, 70 sube al padre
  
       [30 | 70]
      /    |    \
 [10|20]  [50|60]  [80|90]   ✓ todos con ≥ 2 claves
```

---

## 5. Aplicaciones

Los Árboles-B son omnipresentes en sistemas que manejan grandes volúmenes de datos:

- **MySQL / InnoDB**: usa Árboles-B+ (variante) para índices primarios y secundarios.
- **PostgreSQL**: estructura de índice por defecto.
- **SQLite**: toda la base de datos vive en un Árbol-B.
- **Sistemas de archivos**: NTFS, ext4, HFS+.
- **Motores de bases de datos NoSQL**: MongoDB, LevelDB.

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_arbol_b.py`](./ejemplos/01_arbol_b.py) | Árbol-B completo con inserción y split |
| [`ejemplos/02_eliminacion_b.py`](./ejemplos/02_eliminacion_b.py) | Eliminación con préstamo y fusión |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
