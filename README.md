# Binary Search Tree Animation - Proyecto AED

## Presentación del Proyecto

Este proyecto implementa una **animación visual educativa de un Binary Search Tree (Árbol Binario de Búsqueda)** utilizando Manim, una librería de Python especializada en crear animaciones de conceptos matemáticos y de estructuras de datos.

**Autor:** Juan Diego Azabache Liñan  
**Código:** 202110430  
**Curso:** CS2023 - Algoritmos y Estructuras de Datos  
**Institución:** UTEC - Universidad de Ingeniería y Tecnología  
**Fecha:** Septiembre 2026

### Objetivo

El objetivo principal es demostrar de forma visual cómo funcionan las operaciones fundamentales en un Binary Search Tree: inserción de nodos, búsqueda de valores (exitosas y fallidas), y eliminación de elementos. La animación permite entender conceptos complejos de una forma más clara y educativa que solo leer teoría.

### Especificaciones

- **Duración:** 1 minuto 20 segundos
- **Resolución:** 1920x1080 @ 60fps
- **Formato:** MPEG-1
- **Tamaño:** 53 MB
- **Código:** 163 líneas de Python
- **Animaciones:** 152 animaciones complejas

---

## Descripción de la Estructura de Datos: Binary Search Tree

### ¿Qué es un Binary Search Tree?

Un **Binary Search Tree (BST)** es una estructura de datos que organiza información en forma de árbol binario. Cada nodo contiene un valor y referencias a dos hijos: uno izquierdo y uno derecho.

**La propiedad fundamental del BST es:**
- Para cualquier nodo N, **todos los valores en su subárbol izquierdo son menores que N**
- **Todos los valores en su subárbol derecho son mayores que N**

Esta propiedad es lo que hace que los BST sean eficientes para búsquedas.

### Por qué es importante

En un BST balanceado, buscar un valor toma **O(log n)** tiempo, donde n es el número de elementos. Esto es muchísimo mejor que una búsqueda lineal que tomaría O(n) tiempo.

**Ejemplo:** En un árbol con 1 millón de elementos:
- Búsqueda lineal: ~500,000 comparaciones
- Búsqueda en BST: ~20 comparaciones

### Operaciones Principales

#### 1. Inserción
Cuando insertas un valor, comienzas en la raíz. Comparas el valor:
- Si es **menor**, vas al subárbol izquierdo
- Si es **mayor**, vas al subárbol derecho
- Repites recursivamente hasta encontrar la posición correcta

El árbol mantiene automáticamente la propiedad BST sin necesidad de reordenamientos complicados.

#### 2. Búsqueda
Para buscar un valor, sigues el mismo proceso:
- Comparas con cada nodo
- Vas a izquierda o derecha según sea necesario
- Si encuentras el valor, lo localizaste
- Si llegas a una posición vacía, el valor no existe

Esto es mucho más eficiente que revisar cada elemento uno por uno.

#### 3. Eliminación
Es la operación más compleja:
- Si el nodo es una hoja, simplemente lo remueives
- Si tiene un hijo, reemplazas el nodo con su hijo
- Si tiene dos hijos, encuentras el sucesor inorden y lo usas para reemplazar

### Complejidad

| Operación | Promedio | Peor Caso |
|-----------|----------|-----------|
| Búsqueda | O(log n) | O(n) |
| Inserción | O(log n) | O(n) |
| Eliminación | O(log n) | O(n) |

El peor caso ocurre cuando el árbol es degenerado (como una lista enlazada).

---

## Software Requerido

Para compilar y ejecutar este proyecto necesitas:

### Software Obligatorio
- **Python 3.10** o superior
- **Manim Community 0.21.0** (librería de animaciones)
- **FFmpeg** (para procesamiento de video)

### Dependencias del Sistema

**En Windows:**
- Microsoft C++ Build Tools
- (Descargable desde: https://visualstudio.microsoft.com/visual-cpp-build-tools/)

**En macOS:**
- Homebrew (gestor de paquetes)

**En Linux (Ubuntu/Debian):**
- libpango1.0-dev
- libcairo2-dev
- pkg-config

---

## Instalación

### Opción 1: Windows

```bash
# 1. Descargar e instalar Microsoft C++ Build Tools
# https://visualstudio.microsoft.com/visual-cpp-build-tools/

# 2. Descargar Python desde python.org e instalar

# 3. Abrir PowerShell y ejecutar:
pip install manim
```

### Opción 2: macOS

```bash
# 1. Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Instalar dependencias
brew install python ffmpeg

# 3. Instalar Manim
pip install manim
```

### Opción 3: Linux (Ubuntu/Debian)

```bash
# 1. Instalar dependencias del sistema
sudo apt-get install python3 libpango1.0-dev libcairo2-dev pkg-config ffmpeg

# 2. Instalar Manim
pip install manim
```

---

## Compilación y Ejecución

### Compilar en baja calidad (para pruebas rápidas)

```bash
manim -pql Proyecto_AED_JuanAzabache.py BSTAnimation
```

- `-p`: Preview (abre el video automáticamente después)
- `-q`: Quality
- `-l`: Low quality (480p15) - compilación rápida (~30 segundos)

### Compilar en alta calidad (para entrega final)

```bash
manim -pqh Proyecto_AED_JuanAzabache.py BSTAnimation
```

- `-h`: High quality (1080p60) - compilación lenta (~2-3 minutos)

### Compilar sin preview (sin abrir el video)

```bash
manim -qh Proyecto_AED_JuanAzabache.py BSTAnimation
```

### Donde encontrar el video compilado

El video se guarda en:
```
media/videos/bst_animation/1080p60/bst_animation.mp4
```

---

## Lo que ves en el Video

El video está dividido en **6 fases principales:**

### Fase 1: Inserción de Nodos (0-16 segundos)
Se insertan 10 valores: 50, 30, 70, 20, 40, 60, 80, 10, 25, 35 y 45. Cada nodo aparece en su posición correcta, manteniendo la propiedad BST. Nodo raíz en azul, nodos nuevos en verde.

### Fase 2: Primera Búsqueda Exitosa (16-30 segundos)
Se busca el valor 25. El algoritmo recorre el árbol, resaltando cada nodo visitado en amarillo. Cuando encuentra el 25, lo resalta en verde y muestra "¡Encontrado!".

### Fase 3: Búsqueda Fallida (30-45 segundos)
Se intenta buscar el valor 15 (que no existe). El algoritmo recorre hasta una hoja y muestra "No existe" en rojo.

### Fase 4: Segunda Búsqueda Exitosa (45-60 segundos)
Se busca el valor 70, demostrando nuevamente la eficiencia de la búsqueda.

### Fase 5: Eliminación de Nodo (60-70 segundos)
Se elimina el nodo 25. El nodo se resalta en rojo y desaparece.

### Fase 6: Verificación Post-Eliminación (70-80 segundos)
Se intenta buscar nuevamente el valor 25. Ahora no se encuentra, confirmando que fue eliminado.

---

## Estructura del Proyecto

```
Proyecto-AED-Juan-Diego-Azabache/
├── Proyecto_AED_JuanAzabache.py    # Código fuente de la animación
├── README.md                        # Este archivo
└── Proyecto_AED_JuanAzabache.mpeg  # Video compilado
```

---

## Código Principal

El código está organizado en dos clases:

### Clase BSTNode
Representa cada nodo del árbol:
- `value`: Valor almacenado en el nodo
- `left`: Referencia al hijo izquierdo
- `right`: Referencia al hijo derecho
- `pos`: Posición en el canvas
- `mobject_circle`: Objeto visual (círculo)
- `mobject_text`: Objeto visual (texto)

### Clase BSTAnimation
Hereda de `Scene` en Manim. Contiene:
- `construct()`: Método principal que define toda la animación
- `get_tree_position()`: Calcula posiciones automáticamente
- `insert_to_tree()`: Implementa inserción recursiva
- `animate_node_creation()`: Anima la creación de nodos
- `search_value()`: Implementa búsqueda recursiva con animación

---

## Características Técnicas

- **Algoritmo de inserción recursiva:** Mantiene la propiedad BST
- **Algoritmo de búsqueda recursiva:** Recorre eficientemente el árbol
- **Posicionamiento dinámico:** Cada nodo se posiciona según su profundidad
- **Animaciones visuales:** Colores dinámicos para indicar estados
- **Animaciones suaves:** Transiciones de 60 frames por segundo

---

## Requisitos Cumplidos

✅ Usa Manim Community como se requiere  
✅ Demuestra claramente una estructura de datos (BST)  
✅ Video de 1:20 minutos (dentro del rango 1-2 minutos)  
✅ Formato MPEG en alta resolución (1080p)  
✅ Código compilable y ejecutable  
✅ Documentación completa  
✅ Incluye presentación, software requerido, compilación, y descripción del BST

---

## Referencias

- **Manim Documentation:** https://docs.manim.community/
- **3Blue1Brown Channel:** https://www.3blue1brown.com/
- **Introduction to Algorithms (CLRS):** Cormen, Leiserson, Rivest, Stein

---

## Autor

**Juan Diego Azabache Liñan**  
Estudiante de Ciencias de la Computación - UTEC  
Código: 202110430  
Email: juan.azabache@utecstudiantes.edu.pe

---

*Proyecto completado: 26 de Septiembre, 2026*
