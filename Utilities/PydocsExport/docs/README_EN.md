# PydocsExport - Complete Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Architecture](#architecture)
5. [Output Format](#output-format)
6. [API Reference](#api-reference)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)

---

## Introduction

### What is PydocsExport?

**PydocsExport** is a powerful Python module that allows you to export the complete Python documentation installed on your system into multiple e-book formats and text formats.

### Key Features

- ✅ Export to **5 different formats**: TXT, PDF, EPUB, MOBI, HTML
- ✅ Support for **11 paper formats** for PDFs (A0 to A10)
- ✅ **Organized structure** with chapters and index
- ✅ **Multilingual support** in documentation and interface
- ✅ **Detailed export log** in JSON
- ✅ **Simple and intuitive API** for easy integration
- ✅ **CLI interface** (EasyPydocsExport.py) for users

### Use Cases

- Create a complete offline Python documentation
- Generate e-books for e-reader devices
- Create printable PDFs in different formats
- Archive documentation for future reference
- Create educational resources

---

## Installation

### Requirements

- Python 3.6 or higher
- No external dependencies required (uses built-in pydoc)

### Installation Steps

1. **Clone or download** the project directory:
```bash
git clone <repository_url>
cd PydocsExport
```

2. **Verify the structure**:
```bash
ls
# Should display: src/, tests/, docs/, EasyPydocsExport.py
```

3. **Test the installation**:
```bash
python EasyPydocsExport.py --help
```

### Project Structure

```
PydocsExport/
├── src/                          # Main module
│   ├── __init__.py               # Package initialization
│   ├── exporter.py               # Main exporter class
│   ├── formatter.py              # Formatters for different formats
│   └── index_manager.py          # Index manager
├── tests/                        # Unit tests
│   └── test_pydocs_export.py    # Complete test suite
├── docs/                         # Documentation
│   ├── README.md                 # This file (English)
│   ├── README_EN.md              # English documentation
│   ├── README_FR.md              # French documentation
│   ├── README_ES.md              # Spanish documentation
│   ├── README_DE.md              # German documentation
│   └── README_IT.md              # Italian documentation
├── output/                       # Output directory (created at runtime)
├── EasyPydocsExport.py          # Main script for users
└── README.md                     # Initial file
```

---

## Usage

### Basic Usage

#### Via CLI Script (Recommended)

```bash
# Export all formats
python EasyPydocsExport.py

# Export only TXT and HTML
python EasyPydocsExport.py --txt --html

# Export to PDF only
python EasyPydocsExport.py --pdf

# Specify a custom output directory
python EasyPydocsExport.py --output /my/custom/path

# Show help
python EasyPydocsExport.py --help
```

#### Via Python Module

```python
from src.exporter import PydocsExporter

# Create an exporter
exporter = PydocsExporter(output_base_dir="my_documentation")

# Export all formats
results = exporter.export_all()

# Export specific formats
results = exporter.export_all(formats=['txt', 'epub', 'html'])

# Display results
print(results)
```

### Available Options

| Option | Description | Example |
|--------|-------------|---------|
| `--all` | Export all formats | `--all` |
| `--txt` | Plain text format | `--txt` |
| `--pdf` | PDF format (all sizes) | `--pdf` |
| `--epub` | E-book format | `--epub` |
| `--mobi` | Kindle/MOBI format | `--mobi` |
| `--html` | Interactive HTML pages | `--html` |
| `--output [dir]` | Output directory | `--output /path` |
| `--help` | Show help | `--help` |

---

## Architecture

### Main Components

#### 1. PydocsExporter (exporter.py)

**Responsibilities:**
- Orchestration of export process
- Retrieval of pydocs documentation
- Management of paper formats for PDF
- Creation of directory structures

**Supported Paper Formats:**
```
A0:  2384 × 3370 points
A1:  1684 × 2384 points
A2:  1191 × 1684 points
A3:   842 × 1191 points
A4:   595 ×  842 points (Standard)
A5:   420 ×  595 points
A6:   298 ×  420 points
A7:   210 ×  298 points
A8:   148 ×  210 points
A9:   105 ×  148 points
A10:  73  ×  105 points
```

#### 2. Formatters (formatter.py)

Provides formatting classes:

- **TextFormatter**: Simple formatting for TXT
- **PDFFormatter**: Adaptation for different paper formats
- **EbookFormatter**: Structure for EPUB/MOBI

```python
# Usage example
formatter = TextFormatter()
formatter.add_title("My Title", level=1)
formatter.add_paragraph("My content")
formatter.add_code("print('Hello')", language="python")
content = formatter.get_content()
```

#### 3. IndexManager (index_manager.py)

Manages documentation indexes:

- Creation of indexes in TXT, JSON, HTML
- Grouping by categories
- Generation of table of contents

```python
# Usage example
index_mgr = IndexManager()
index_mgr.add_entry("module_name", "path/to/file", "builtins", 1024)
index_mgr.create_index_file(Path("output"), format="html")
```

---

## Output Format

### Directory Structure

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
│   └── ... (other paper formats)
│
├── EBOOK_EPUB/
│   └── Python_Documentation_[timestamp].epub
│
├── EBOOK_MOBI/
│   └── Python_Documentation_[timestamp].mobi
│
├── HTML/
│   ├── index.html (Interactive index)
│   ├── 001_sys.html
│   ├── 002_os.html
│   └── ...
│
├── INDEX.txt (General index)
└── export_log_[timestamp].json (Export log)
```

### Log File Content

```json
{
  "timestamp": "20240115_143052",
  "formats": {
    "txt": {
      "format": "TXT",
      "files_created": 42,
      "total_size": 5242880,
      "chapters": [
        {
          "name": "sys",
          "file": "001_sys.txt",
          "size": 125440
        }
      ]
    }
  },
  "total_modules": 42,
  "errors": []
}
```

---

## API Reference

### PydocsExporter

#### Constructor

```python
PydocsExporter(output_base_dir: str = "pydocs_export_output")
```

**Parameters:**
- `output_base_dir`: Base directory for exports

#### Method: export_all()

```python
export_all(formats: Optional[List[str]] = None) -> Dict[str, any]
```

**Parameters:**
- `formats`: List of formats to export ('txt', 'pdf', 'epub', 'mobi', 'html')
  - If `None`, all formats are exported

**Returns:**
- Dictionary containing export statistics

**Example:**
```python
exporter = PydocsExporter()
results = exporter.export_all(['txt', 'html'])
print(results['total_modules'])  # Display module count
```

### TextFormatter

```python
# Create a formatter
formatter = TextFormatter()

# Add content
formatter.add_title("My Title", level=1)      # Level 1 title
formatter.add_title("Subtitle", level=2)      # Level 2 title
formatter.add_paragraph("A paragraph")        # Paragraph
formatter.add_code("python code", "python")   # Code block

# Get content
content = formatter.get_content()
```

### IndexManager

```python
# Create an index manager
index_mgr = IndexManager()

# Add entries
index_mgr.add_entry(
    name="my_module",
    path="path/to/file",
    category="builtins",
    file_size=1024,
    module_type="built-in"
)

# Create an index file
index_mgr.create_index_file(Path("output"), format="html")
```

---

## Examples

### Example 1: Simple Export

```bash
python EasyPydocsExport.py
```

This will export all documentation in all available formats
to the default directory `pydocs_export_output/`.

### Example 2: Specific Export

```bash
python EasyPydocsExport.py --txt --html --output /my/folder
```

Export only TXT and HTML to `/my/folder/`.

### Example 3: Programmatic Usage

```python
#!/usr/bin/env python3
from pathlib import Path
from src.exporter import PydocsExporter

def main():
    # Create an exporter
    exporter = PydocsExporter("my_documentation")
    
    # Export
    print("Starting export...")
    results = exporter.export_all(['epub', 'mobi'])
    
    # Display stats
    print(f"Exported modules: {results['total_modules']}")
    for fmt, stats in results['formats'].items():
        print(f"{fmt}: {stats}")

if __name__ == "__main__":
    main()
```

### Example 4: Custom Processing

```python
from src.exporter import PydocsExporter
from src.index_manager import IndexManager
from pathlib import Path

# Create the exporter
exporter = PydocsExporter()

# Get module list
modules = exporter._get_all_modules()

# Create a custom index
index = IndexManager()
for module in modules[:10]:  # First 10 modules
    index.add_entry(module, f"modules/{module}.txt", "demo", 1024)

# Save index as HTML
index.create_index_file(exporter.output_base, format="html")
```

---

## Troubleshooting

### Issue: "Unable to import PydocsExporter module"

**Solution:**
1. Verify you're in the correct directory
2. Check that the `src/` directory exists
3. Check that `__init__.py` is in `src/`

```bash
ls -la src/
# Should display __init__.py
```

### Issue: Permission denied when creating files

**Solution:**
1. Check output directory permissions
2. Use a different directory with `--output`

```bash
# Create a directory with permissions
mkdir -p ~/my_docs
python EasyPydocsExport.py --output ~/my_docs
```

### Issue: Output files corrupted or empty

**Solution:**
1. Check available disk space
2. Check error logs in `export_log_[timestamp].json`
3. Try exporting a single format

```bash
python EasyPydocsExport.py --txt
```

### Issue: Export is very slow

**Solution:**
- This is normal for a complete first export
- There are many modules (100+)
- Be patient or reduce the number of modules in `exporter.py`

---

## Contributing

### Report a Bug

1. Open an issue with:
   - Description of the problem
   - Steps to reproduce
   - Environment (OS, Python version)

### Propose an Enhancement

1. Fork the project
2. Create a branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Run Tests

```bash
python -m pytest tests/ -v
# or
python tests/test_pydocs_export.py
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Support

For any questions or support:
- 📧 Email: support@pydocsexport.local
- 🐛 Issues: https://github.com/example/pydocsexport/issues
- 💬 Discussions: https://github.com/example/pydocsexport/discussions

---

**Last Updated:** January 2024
**Version:** 1.0.0
**Maintained By:** Copilot

---

## Additional Resources

### Official Python Documentation
- [pydoc](https://docs.python.org/3/library/pydoc.html)
- [Built-in Modules](https://docs.python.org/3/library/index.html)

### E-Book Formats
- [EPUB Format](https://www.w3.org/publishing/epub/)
- [MOBI Format](https://wiki.mobileread.com/wiki/MOBI)

### Other Tools
- [Sphinx](https://www.sphinx-doc.org/) - Documentation Generator
- [Pandoc](https://pandoc.org/) - Document Converter

---

**Thank you for using PydocsExport! 🎉**
