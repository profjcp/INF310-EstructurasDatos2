# 📚 INF-310 | Estructuras de Datos II

> **Prof. Juan Carlos Peinado · Universidad · 5to Semestre  
> Código en **Python** · Teoría + Ejercicios + Proyectos

---

## 🎯 ¿De qué trata este curso?

Este repositorio es el material completo del curso **Estructuras de Datos II (INF-310)**. Aquí encontrarás teoría, código de ejemplo en Python y ejercicios para aprender de forma autodidacta las estructuras de datos **no lineales**.

> **Requisito:** Haber cursado INF-220 Estructuras de Datos I (listas, pilas, colas, etc.)

---

## 🧭 Índice General

- [📂 Contenido del Repositorio](#-contenido-del-repositorio)
- [🗂️ Estructura de cada Unidad](#️-estructura-de-cada-unidad)
- [🚀 Proyectos Finales](#-proyectos-finales)
- [⚙️ Cómo usar este repositorio](#️-cómo-usar-este-repositorio)
- [📋 Sistema de Evaluación](#-sistema-de-evaluación)
- [📚 Bibliografía](#-bibliografía)
- [👨‍🏫 Docente](#-docente)

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
    └── soluciones/
```

---

## 🚀 Proyectos Finales

Para el cierre de la materia, los estudiantes pueden desarrollar uno de los siguientes proyectos:

### 1) Sistema de rutas de transporte (Grafos pesados)
- Modelar una red de paradas y rutas con pesos (distancia, tiempo o costo).
- Implementar cálculo de rutas óptimas entre origen y destino.
- Estructuras/algoritmos sugeridos: grafo con listas de adyacencia, Dijkstra, BFS/DFS.

### 2) Motor de búsqueda de registros (ABB + Árboles M-Vías/B)
- Gestionar un conjunto grande de registros (contactos, libros, productos, etc.).
- Permitir inserción, eliminación, búsqueda por clave y recorridos ordenados.
- Comparar desempeño entre ABB y una alternativa M-vías o Árbol-B en distintos tamaños de datos.

### 3) Planificador académico con prerrequisitos (Grafo dirigido)
- Representar materias y dependencias de prerrequisitos como un grafo dirigido.
- Validar si existen ciclos y proponer un orden de cursado por semestres.
- Estructuras/algoritmos sugeridos: detección de ciclos, orden topológico, BFS/DFS.

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
