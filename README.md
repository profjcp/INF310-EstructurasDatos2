# 📚 INF-310 | Estructuras de Datos II

> **Prof. Juan Carlos Peinado · Universidad · 5to Semestre  
> Código en **Python** · Teoría + Ejercicios + Proyectos

---

## 🎯 ¿De qué trata este curso?

Este repositorio es el material completo del curso **Estructuras de Datos II (INF-310)**. Aquí encontrarás teoría, código de ejemplo en Python y ejercicios para aprender de forma autodidacta las estructuras de datos **no lineales**.

> **Requisito:** Haber cursado INF-220 Estructuras de Datos I (listas, pilas, colas, etc.)

---

## 🧭 Índice General

- [🗺️ Mapa Conceptual del Curso](#️-mapa-conceptual-del-curso)
- [🛠️ Recursos Transversales](#️-recursos-transversales)

---

## 📂 Contenido del Repositorio

| Unidad/Sección | Tema | Horas |
|----------------|------|-------|
| [Unidad 0](./unidad0/) | Estándares y Buenas Prácticas de Codificación | — |
| [Unidad I](./unidad1/) | Árboles Binarios de Búsqueda (ABB) | 24 hs |
| [Unidad II](./unidad2/) | Árboles M-Vías | 18 hs |
| [Unidad III](./unidad3/) | Árboles-B | 24 hs |
| [Unidad IV](./unidad4/) | Grafos | 18 hs |
| [Unidad V](./unidad5/) | Grafos Pesados y Algoritmos Clásicos | 12 hs |
| [Proyectos Finales](#-proyectos-finales) | Propuestas integradoras del curso | 15% |

---

## 🗺️ Mapa Conceptual del Curso

Las unidades no son independientes: cada una construye sobre la anterior.
Entender estas conexiones ayuda a estudiar con contexto.

```
Unidad 0 ── Buenas Prácticas (base para todo el código del curso)

Unidad I  ── ABB (árbol binario con propiedad de ordenamiento)
    │           ↳ Inserción O(h), Búsqueda O(h), pero h puede ser n en peor caso
    │
    ▼
Unidad II ── Árbol M-Vías (generalización: cada nodo tiene hasta m hijos)
    │           ↳ Reduce la altura: log_m(n) en vez de log_2(n)
    │           ↳ Sin control de balanceo → puede degenerarse igual que ABB
    │
    ▼
Unidad III ── Árbol-B (M-Vías + balanceo garantizado)
                ↳ Todas las hojas al mismo nivel → h = O(log_m n) siempre
                ↳ Usado en sistemas de archivos y bases de datos (acceso a disco)

Unidad IV ── Grafos (estructura más general: nodos + aristas, sin jerarquía)
    │           ↳ Los árboles son un caso especial de grafos (acíclicos y conexos)
    │           ↳ BFS y DFS como recorridos base
    │
    ▼
Unidad V  ── Grafos Pesados (aristas con costo/distancia/tiempo)
                ↳ Dijkstra: camino mínimo desde un origen → O((V+E) log V)
                ↳ Floyd-Warshall: camino mínimo entre todos los pares → O(V³)
                ↳ Prim / Kruskal: árbol de expansión mínima → O(E log V)
```

> **Regla de oro:** si el problema involucra jerarquía y ordenamiento → árboles.
> Si involucra relaciones entre pares de entidades → grafos.

---

## 🗂️ Estructura de cada Unidad

Cada carpeta de unidad contiene:

```
unidadX/
├── README.md        ← Teoría completa de la unidad
├── ejemplos/        ← Código Python comentado
│   ├── 01_ejemplo.py
│   └── 02_ejemplo.py
└── ejercicios/      ← Problemas para practicar
    ├── enunciados.md
    ├── plantilla_ejNN_nombre.py  ← Archivo de arranque con tests automáticos
    └── soluciones/
```

---

## 🛠️ Recursos Transversales

### `utils/visualizar.py`
Funciones reutilizables para visualizar estructuras en consola. Disponibles en todas las unidades:

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.visualizar import imprimir_arbol, imprimir_arbol_b, imprimir_grafo, imprimir_matriz

# Árbol binario (Unidad I)
imprimir_arbol(abb._raiz)

# Árbol-B o M-Vías (Unidades II y III)
imprimir_arbol_b(arbol_b._raiz)

# Grafo (Unidades IV y V)
imprimir_grafo(grafo._adyacencia, pesos=True)

# Matriz de distancias Floyd-Warshall
imprimir_matriz(dist, titulo="Distancias mínimas")
```

### `datos/` — Datasets reales para los proyectos

| Archivo | Proyecto | Descripción |
|---------|----------|-------------|
| `datos/red_metro_paradas.csv` | Proyecto 1 | 15 paradas de transporte urbano con coordenadas |
| `datos/red_metro_rutas.csv` | Proyecto 1 | Rutas entre paradas con distancia, tiempo y costo |
| `datos/catalogo_libros.csv` | Proyecto 2 | 20 libros técnicos con ISBN, autor, año y disponibilidad |
| `datos/malla_materias.csv` | Proyecto 3 | 15 materias con código, semestre y créditos |
| `datos/malla_prerrequisitos.csv` | Proyecto 3 | Relaciones de prerrequisito entre materias |

### Modo verbose en algoritmos (Unidad V)
Dijkstra y Floyd-Warshall aceptan `verbose=True` para imprimir cada paso:

```python
# Ver la tabla de Dijkstra paso a paso
distancias, pred = dijkstra(grafo, origen="A", verbose=True)

# Ver la evolución de la matriz en Floyd-Warshall
dist, next_hop = floyd_warshall(vertices, aristas, verbose=True)
```

---

## 🚀 Proyectos Finales

Para el cierre de la materia, los estudiantes pueden desarrollar uno de los siguientes proyectos:

### 1) Sistema de rutas de transporte (Grafos pesados)
- Modelar una red de paradas y rutas con pesos (distancia, tiempo o costo).
- Implementar cálculo de rutas óptimas entre origen y destino.
- Estructuras/algoritmos sugeridos: grafo con listas de adyacencia, Dijkstra, BFS/DFS.
- **Dataset provisto:** `datos/red_metro_paradas.csv` y `datos/red_metro_rutas.csv`

### 2) Motor de búsqueda de registros (ABB + Árboles M-Vías/B)
- Gestionar un conjunto grande de registros (contactos, libros, productos, etc.).
- Permitir inserción, eliminación, búsqueda por clave y recorridos ordenados.
- Comparar desempeño entre ABB y una alternativa M-vías o Árbol-B en distintos tamaños de datos.
- **Dataset provisto:** `datos/catalogo_libros.csv` (20 libros técnicos)

### 3) Planificador académico con prerrequisitos (Grafo dirigido)
- Representar materias y dependencias de prerrequisitos como un grafo dirigido.
- Validar si existen ciclos y proponer un orden de cursado por semestres.
- Estructuras/algoritmos sugeridos: detección de ciclos, orden topológico, BFS/DFS.
- **Dataset provisto:** `datos/malla_materias.csv` y `datos/malla_prerrequisitos.csv`

### 📋 Rúbrica de evaluación de proyectos

| Criterio | Insuficiente (0–49%) | Suficiente (50–74%) | Sobresaliente (75–100%) |
|----------|----------------------|---------------------|--------------------------|
| **Correctitud del algoritmo** | No implementado o falla en casos básicos | Funciona en el caso feliz; falla en casos borde | Maneja todos los casos, incluyendo grafos vacíos y datos inválidos |
| **Uso correcto de la estructura** | Usa listas/diccionarios sin ABB/grafo | Usa la estructura pero sin aprovechar sus propiedades | Justifica por qué eligió esa estructura sobre otras alternativas |
| **Análisis de complejidad** | Ausente | Menciona la notación O() de las operaciones principales | Justifica con medición empírica (tiempo de ejecución vs. n) |
| **Lectura del dataset real** | No usa el CSV provisto | Lee el CSV pero con código frágil | Lee, valida y documenta el formato esperado |
| **Documentación** | Sin comentarios ni docstrings | Docstrings en las funciones principales | Docstrings completos + ejemplo de uso en `if __name__ == "__main__"` |

---

## ⚙️ Cómo usar este repositorio

### Clonar el repositorio
```bash
git clone https://github.com/profjcp/INF310-EstructurasDatos2.git
cd INF310-EstructurasDatos2
```

### Requisitos
- Python 3.8 o superior
- No se requieren librerías externas para la mayoría de ejemplos

```bash
python --version   # Verificar versión
```

### Ejecutar un ejemplo
```bash
cd unidad1/ejemplos
python 01_nodo_arbol.py
```

---

## 📋 Sistema de Evaluación

| Componente | Porcentaje |
|------------|-----------|
| 2 Exámenes Parciales | 60% |
| Proyectos | 15% |
| Examen Final | 25% |

---

## 📚 Bibliografía

- T.G. Lewis y M.Z. Smith — *Estructuras de Datos*, Ed. Paraninfo
- L. Joyanes Aguilar e I. Zahonero Martínez — *Estructuras de Datos*
- A.M. Tenenbaum — *Estructuras de Datos en C*, Prentice Hall
- R.L. Kruse — *Estructuras de Datos y Diseño de Programas*, Prentice Hall
- J.P. Tremblay — *An Introduction to Data Structures with Applications*

---

## 👨‍🏫 Docente

**Prof. Juan Carlos Peinado  
🔗 [github.com/profjcp](https://github.com/profjcp)

---

> 💡 ¿Encontraste un error o tienes una mejora? Abre un **Issue** o envía un **Pull Request**.
