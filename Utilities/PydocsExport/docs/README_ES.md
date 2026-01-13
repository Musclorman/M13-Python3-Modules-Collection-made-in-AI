# PydocsExport - Documentación Completa

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Arquitectura](#arquitectura)
5. [Formato de Salida](#formato-de-salida)
6. [Referencia de API](#referencia-de-api)
7. [Ejemplos](#ejemplos)
8. [Solución de Problemas](#solución-de-problemas)
9. [Contribuir](#contribuir)

---

## Introducción

### ¿Qué es PydocsExport?

**PydocsExport** es un módulo Python poderoso que permite exportar la documentación completa de Python instalada en su sistema en múltiples formatos de libros electrónicos y formatos de texto.

### Características Principales

- ✅ Exportación a **5 formatos diferentes**: TXT, PDF, EPUB, MOBI, HTML
- ✅ Soporte para **11 formatos de papel** para PDFs (A0 a A10)
- ✅ **Estructura organizada** con capítulos e índice
- ✅ **Soporte multilingüe** en documentación e interfaz
- ✅ **Registro de exportación detallado** en JSON
- ✅ **API simple e intuitiva** para fácil integración
- ✅ **Interfaz CLI** (EasyPydocsExport.py) para usuarios

### Casos de Uso

- Crear documentación completa de Python sin conexión
- Generar libros electrónicos para dispositivos de lectura
- Crear PDFs imprimibles en diferentes formatos
- Archivar documentación para referencia futura
- Crear recursos educativos

---

## Instalación

### Requisitos

- Python 3.6 o superior
- Sin dependencias externas requeridas (usa pydoc integrado)

### Pasos de Instalación

1. **Clonar o descargar** el directorio del proyecto:
```bash
git clone <repository_url>
cd PydocsExport
```

2. **Verificar la estructura**:
```bash
ls
# Debe mostrar: src/, tests/, docs/, EasyPydocsExport.py
```

3. **Probar la instalación**:
```bash
python EasyPydocsExport.py --help
```

### Estructura del Proyecto

```
PydocsExport/
├── src/                          # Módulo principal
│   ├── __init__.py               # Inicialización del paquete
│   ├── exporter.py               # Clase exportadora principal
│   ├── formatter.py              # Formateadores para diferentes formatos
│   └── index_manager.py          # Gestor de índices
├── tests/                        # Pruebas unitarias
│   └── test_pydocs_export.py    # Suite de pruebas completa
├── docs/                         # Documentación
│   ├── README.md                 # Este archivo (Español)
│   ├── README_EN.md              # Documentación en inglés
│   ├── README_FR.md              # Documentación en francés
│   ├── README_ES.md              # Documentación en español
│   ├── README_DE.md              # Documentación en alemán
│   └── README_IT.md              # Documentación en italiano
├── output/                       # Directorio de salida (creado en tiempo de ejecución)
├── EasyPydocsExport.py          # Script principal para usuarios
└── README.md                     # Archivo inicial
```

---

## Uso

### Uso Básico

#### Via Script CLI (Recomendado)

```bash
# Exportar todos los formatos
python EasyPydocsExport.py

# Exportar solo TXT y HTML
python EasyPydocsExport.py --txt --html

# Exportar solo a PDF
python EasyPydocsExport.py --pdf

# Especificar un directorio de salida personalizado
python EasyPydocsExport.py --output /mi/ruta/personalizada

# Mostrar ayuda
python EasyPydocsExport.py --help
```

#### Via Módulo Python

```python
from src.exporter import PydocsExporter

# Crear un exportador
exportador = PydocsExporter(output_base_dir="mi_documentacion")

# Exportar todos los formatos
resultados = exportador.export_all()

# Exportar formatos específicos
resultados = exportador.export_all(formats=['txt', 'epub', 'html'])

# Mostrar resultados
print(resultados)
```

### Opciones Disponibles

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `--all` | Exportar todos los formatos | `--all` |
| `--txt` | Formato de texto plano | `--txt` |
| `--pdf` | Formato PDF (todos los tamaños) | `--pdf` |
| `--epub` | Formato de libro electrónico | `--epub` |
| `--mobi` | Formato Kindle/MOBI | `--mobi` |
| `--html` | Páginas HTML interactivas | `--html` |
| `--output [dir]` | Directorio de salida | `--output /ruta` |
| `--help` | Mostrar ayuda | `--help` |

---

## Arquitectura

### Componentes Principales

#### 1. PydocsExporter (exporter.py)

**Responsabilidades:**
- Orquestación del proceso de exportación
- Recuperación de documentación de pydocs
- Gestión de formatos de papel para PDF
- Creación de estructuras de directorios

**Formatos de Papel Soportados:**
```
A0:  2384 × 3370 puntos
A1:  1684 × 2384 puntos
A2:  1191 × 1684 puntos
A3:   842 × 1191 puntos
A4:   595 ×  842 puntos (Estándar)
A5:   420 ×  595 puntos
A6:   298 ×  420 puntos
A7:   210 ×  298 puntos
A8:   148 ×  210 puntos
A9:   105 ×  148 puntos
A10:  73  ×  105 puntos
```

#### 2. Formateadores (formatter.py)

Proporciona clases de formateo:

- **TextFormatter**: Formateo simple para TXT
- **PDFFormatter**: Adaptación para diferentes formatos de papel
- **EbookFormatter**: Estructura para EPUB/MOBI

```python
# Ejemplo de uso
formateador = TextFormatter()
formateador.add_title("Mi Título", level=1)
formateador.add_paragraph("Mi contenido")
formateador.add_code("print('Hola')", language="python")
contenido = formateador.get_content()
```

#### 3. Gestor de Índices (index_manager.py)

Gestiona índices de documentación:

- Creación de índices en TXT, JSON, HTML
- Agrupación por categorías
- Generación de tabla de contenidos

```python
# Ejemplo de uso
gestor_indice = IndexManager()
gestor_indice.add_entry("nombre_modulo", "ruta/al/archivo", "integrados", 1024)
gestor_indice.create_index_file(Path("salida"), format="html")
```

---

## Formato de Salida

### Estructura de Directorios

```
pydocs_export_output/
│
├── TXT/
│   ├── Chapters/
│   │   ├── 001_sys.txt
│   │   ├── 002_os.txt
│   │   └── ...
│   └── index.txt
│
├── PDF/
│   ├── A0/
│   │   └── Python_Documentation_A0_[timestamp].txt
│   ├── A1/
│   │   └── Python_Documentation_A1_[timestamp].txt
│   ├── A3/
│   │   └── Python_Documentation_A3_[timestamp].txt
│   ├── A4/
│   │   └── Python_Documentation_A4_[timestamp].txt
│   └── ... (otros formatos de papel)
│
├── EBOOK_EPUB/
│   └── Python_Documentation_[timestamp].epub
│
├── EBOOK_MOBI/
│   └── Python_Documentation_[timestamp].mobi
│
├── HTML/
│   ├── index.html (Índice interactivo)
│   ├── 001_sys.html
│   ├── 002_os.html
│   └── ...
│
├── INDEX.txt (Índice general)
└── export_log_[timestamp].json (Registro de exportación)
```

---

## Ejemplos

### Ejemplo 1: Exportación Simple

```bash
python EasyPydocsExport.py
```

Esto exportará toda la documentación en todos los formatos disponibles
al directorio predeterminado `pydocs_export_output/`.

### Ejemplo 2: Exportación Específica

```bash
python EasyPydocsExport.py --txt --html --output /mi/carpeta
```

Exporta solo TXT y HTML a `/mi/carpeta/`.

### Ejemplo 3: Uso Programático

```python
#!/usr/bin/env python3
from pathlib import Path
from src.exporter import PydocsExporter

def main():
    # Crear un exportador
    exportador = PydocsExporter("mi_documentacion")
    
    # Exportar
    print("Iniciando exportación...")
    resultados = exportador.export_all(['epub', 'mobi'])
    
    # Mostrar estadísticas
    print(f"Módulos exportados: {resultados['total_modules']}")
    for fmt, stats in resultados['formats'].items():
        print(f"{fmt}: {stats}")

if __name__ == "__main__":
    main()
```

---

## Solución de Problemas

### Problema: Error "Imposible importar módulo PydocsExporter"

**Solución:**
1. Verifique que esté en el directorio correcto
2. Verifique que el directorio `src/` existe
3. Verifique que `__init__.py` está en `src/`

```bash
ls -la src/
# Debe mostrar __init__.py
```

### Problema: Permiso denegado al crear archivos

**Solución:**
1. Verifique permisos del directorio de salida
2. Use otro directorio con `--output`

```bash
mkdir -p ~/mis_docs
python EasyPydocsExport.py --output ~/mis_docs
```

---

## Licencia

Este proyecto está bajo licencia MIT. Consulte el archivo `LICENSE` para más detalles.

---

**Última actualización:** Enero 2024
**Versión:** 1.0.0

---

**¡Gracias por usar PydocsExport! 🎉**
