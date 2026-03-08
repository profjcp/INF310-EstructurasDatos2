# Unidad II · Árboles M-Vías

**Tiempo estimado:** 18 horas

## 🎯 Objetivo

Comprender y valorar la importancia de la búsqueda multivía que se presenta en muchas aplicaciones, en especial las de Bases de Datos.

---

## 1. Conceptos

### Limitación de los ABB

Los Árboles Binarios de Búsqueda tienen un problema fundamental: cuando almacenamos **millones de registros en disco**, cada comparación implica un acceso al disco (muy lento). En un ABB con 1 millón de nodos, necesitamos hasta **20 accesos a disco** para encontrar un elemento.

**Solución:** Aumentar el número de hijos por nodo → árbol más "ancho" y menos "alto" → **menos accesos a disco**.

### ¿Qué es un Árbol M-Vía?

Un **Árbol M-Vía** (también llamado árbol de orden m o árbol m-ario) es una generalización del ABB donde cada nodo puede tener hasta **m hijos** y almacenar hasta **m-1 claves**.

Para m = 2 → árbol binario (caso especial)  
Para m = 5 → cada nodo tiene hasta 5 hijos y 4 claves

### Estructura de un nodo en un árbol m-vío

```
Nodo de orden 5 (m=5):

┌────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ P0 │ K1 │ P1 │ K2 │ P2 │ K3 │ P3 │ K4 │ P4 │
└────┴────┴────┴────┴────┴────┴────┴────┴────┘
 ptr  clave ptr  clave ptr  clave ptr  clave ptr

Donde:
  Ki = clave i (dato almacenado)
  Pi = puntero al subárbol i
  
Invariante: K1 < K2 < K3 < K4
            todos los datos en P0 < K1
            K1 < todos los datos en P1 < K2
            K2 < todos los datos en P2 < K3
            ...
```

### Propiedad de ordenamiento generalizada

Para un nodo con claves K₁ < K₂ < ... < Kₙ y punteros P₀, P₁, ..., Pₙ:

- Todos los valores en el subárbol P₀ < K₁
- K₁ < todos los valores en subárbol P₁ < K₂
- Kᵢ < todos los valores en subárbol Pᵢ < Kᵢ₊₁
- Kₙ < todos los valores en el subárbol Pₙ

### Ventaja sobre ABB

```
Comparación para 1,000,000 registros:

ABB (orden 2):  altura ≈ log₂(1,000,000) ≈ 20  → 20 accesos a disco
Árbol (orden 100): altura ≈ log₁₀₀(1,000,000) ≈ 3  → solo 3 accesos a disco!
```

---

## 2. Operaciones de los Árboles M-Vías

### 2.1 Búsqueda

La búsqueda es similar al ABB pero en cada nodo buscamos entre m-1 claves:

```
Buscar K en un árbol de orden m:

1. Si el nodo es None → no encontrado
2. Buscar K entre las claves K1, K2, ..., Kn del nodo actual
3. Si K == Ki → ¡encontrado!
4. Si K < K1 → buscar recursivamente en P0
5. Si Ki < K < Ki+1 → buscar recursivamente en Pi
6. Si K > Kn → buscar recursivamente en Pn
```

**Complejidad:** O(m × h) donde h = altura. Como h ≈ logₘ(n), el costo total es O(m × logₘ(n)).

### 2.2 Inserción

La inserción en un árbol m-vío **sin restricciones** es simple:

1. Buscar la hoja donde insertar.
2. Insertar la clave en orden dentro del nodo.
3. Si el nodo tiene menos de m-1 claves → listo.
4. Si el nodo se llena (m-1 claves) → ⚠️ **problema del desbalance** (se resuelve en Unidad III con Árboles-B).

---

## 3. Recorridos en los Árboles M-Vías

### Recorrido en-orden generalizado

Visitar P₀, luego K₁, luego P₁, luego K₂, ..., hasta Kₙ, luego Pₙ.

```python
def en_orden(self, nodo, resultado):
    if nodo is None:
        return
    for i in range(len(nodo.claves)):
        self.en_orden(nodo.hijos[i], resultado)   # subárbol izquierdo de Ki
        resultado.append(nodo.claves[i])           # clave Ki
    self.en_orden(nodo.hijos[-1], resultado)       # último subárbol
```

### Recorrido por niveles (BFS)

Igual que en ABB pero encolando todos los hijos de cada nodo.

---

## 4. Aplicaciones

Los árboles m-vías son la base de las estructuras de indexación en bases de datos:

- **Índices de bases de datos**: MySQL, PostgreSQL usan variantes de árboles m-vías.
- **Sistemas de archivos**: NTFS (Windows) y HFS+ (Mac) usan B-Trees.
- **Motores de búsqueda**: índices invertidos con estructura de árbol.
- **Cachés de disco**: minimizar lecturas físicas del disco duro.

---

## 📁 Archivos de esta unidad

| Archivo | Descripción |
|---------|-------------|
| [`ejemplos/01_nodo_mvias.py`](./ejemplos/01_nodo_mvias.py) | Clase Nodo para árbol m-vía |
| [`ejemplos/02_arbol_mvias.py`](./ejemplos/02_arbol_mvias.py) | Árbol m-vía con búsqueda e inserción |
| [`ejercicios/enunciados.md`](./ejercicios/enunciados.md) | Ejercicios propuestos |
