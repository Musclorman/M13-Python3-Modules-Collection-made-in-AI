# PydocsExport

> 📚 Export your complete Python documentation to multiple e-book and text formats!

## Quick Start

```bash
# Export all formats with one command
python EasyPydocsExport.py

# Export specific formats
python EasyPydocsExport.py --txt --html --output ~/my_docs

# View help
python EasyPydocsExport.py --help
```

## What is PydocsExport?

PydocsExport is a powerful Python module that allows you to export the complete Python documentation installed on your system into multiple formats:

- 📄 **TXT** - Plain text with organized chapters
- 📕 **PDF** - All 11 paper sizes (A0 to A10)
- 📱 **EPUB** - E-reader format (iPad, Kobo, etc.)
- 📖 **MOBI** - Kindle format
- 🌐 **HTML** - Interactive web pages

## Features

✨ **5 Export Formats** - Generate documentation in your preferred format

🗂️ **Organized Structure** - Chapters, indexes, and table of contents automatically created

🌍 **Multilingual** - Documentation available in English, French, Spanish, German, and Italian

📊 **Detailed Logs** - JSON export logs for tracking and debugging

🚀 **Easy to Use** - Simple CLI interface for non-programmers

💻 **Programmable API** - Integration with your Python code

## Installation

### Requirements
- Python 3.6+
- No external dependencies!

### Setup
```bash
git clone <repository>
cd PydocsExport
python EasyPydocsExport.py --help
```

## Usage Examples

### Basic Usage
```bash
# Export everything to default location
python EasyPydocsExport.py
```

### Export Specific Formats
```bash
# TXT only
python EasyPydocsExport.py --txt

# PDF only
python EasyPydocsExport.py --pdf

# Multiple formats
python EasyPydocsExport.py --txt --epub --html

# PDF with custom location
python EasyPydocsExport.py --pdf --output /my/custom/path
```

### Programmatic Usage
```python
from src.exporter import PydocsExporter

# Create exporter
exporter = PydocsExporter()

# Export to all formats
results = exporter.export_all()

# Export specific formats
results = exporter.export_all(formats=['epub', 'mobi'])

# Access results
print(f"Exported {results['total_modules']} modules")
print(f"Formats: {list(results['formats'].keys())}")
```

## Project Structure

```
PydocsExport/
├── src/
│   ├── exporter.py          # Main export engine
│   ├── formatter.py         # Format-specific handlers
│   └── index_manager.py     # Index generation
├── tests/
│   └── test_pydocs_export.py # Complete test suite
├── docs/
│   ├── README_EN.md         # English docs
│   ├── README_FR.md         # French docs
│   ├── README_ES.md         # Spanish docs
│   ├── README_DE.md         # German docs
│   └── README_IT.md         # Italian docs
├── EasyPydocsExport.py      # User-friendly CLI
└── README.md                # This file
```

## Output Structure

After running the export, you'll get:

```
pydocs_export_output/
├── TXT/
│   ├── Chapters/            # Individual module files
│   └── index.txt            # Index
├── PDF/
│   ├── A0/                  # A0 paper size
│   ├── A4/                  # A4 paper size (standard)
│   └── ... (other sizes)
├── EBOOK_EPUB/              # EPUB format
├── EBOOK_MOBI/              # MOBI format
├── HTML/
│   ├── index.html           # Interactive index
│   └── ... (module pages)
├── INDEX.txt                # General index
└── export_log_*.json        # Detailed log
```

## Supported Paper Sizes (for PDF)

- **A0** (2384 × 3370)
- **A1** (1684 × 2384)
- **A2** (1191 × 1684)
- **A3** (842 × 1191)
- **A4** (595 × 842) - Standard
- **A5** (420 × 595)
- **A6** (298 × 420)
- **A7** (210 × 298)
- **A8** (148 × 210)
- **A9** (105 × 148)
- **A10** (73 × 105)

## API Reference

### Main Class: PydocsExporter

```python
from src.exporter import PydocsExporter

# Initialize
exporter = PydocsExporter(output_base_dir="my_docs")

# Export
results = exporter.export_all(formats=['txt', 'pdf', 'epub', 'mobi', 'html'])

# Results structure:
# {
#     "timestamp": "20240115_143052",
#     "formats": {...},
#     "total_modules": 100,
#     "errors": []
# }
```

### Formatters

```python
from src.formatter import TextFormatter, PDFFormatter, EbookFormatter

# Text formatting
txt_fmt = TextFormatter()
txt_fmt.add_title("Chapter 1", level=1)
txt_fmt.add_paragraph("Content here")
txt_fmt.add_code("python code", language="python")

# PDF formatting with paper sizes
pdf_fmt = PDFFormatter()
pdf_fmt.format_for_paper_size(content, "A4")

# E-book formatting
epub_fmt = EbookFormatter()
epub_fmt.format_epub_chapter("Title", "content")
```

### Index Management

```python
from src.index_manager import IndexManager
from pathlib import Path

# Create index
index = IndexManager()
index.add_entry("module_name", "path/to/file", "category", 1024)

# Generate files
index.create_index_file(Path("output"), format="html")  # html, json, or txt
```

## Testing

Run the comprehensive test suite:

```bash
python tests/test_pydocs_export.py
```

The test suite includes:
- Unit tests for all components
- Integration tests
- Performance tests
- Error handling tests
- 50+ test cases covering all functionality

## Documentation

Full documentation available in multiple languages:

- [English](docs/README_EN.md)
- [Français](docs/README_FR.md)
- [Español](docs/README_ES.md)
- [Deutsch](docs/README_DE.md)
- [Italiano](docs/README_IT.md)

## Common Issues

**Q: "Module not found" error?**
A: Make sure you're in the correct directory and `src/` folder exists.

**Q: Permission denied when creating files?**
A: Use `--output` to specify a writable directory.

**Q: Export is slow?**
A: First export can take time (100+ modules). Subsequent runs are faster.

**Q: How to limit number of modules?**
A: Edit `exporter.py` and change the slicing in `_get_all_modules()`.

## Performance

- **First export**: ~5-10 seconds (all formats)
- **Single format**: ~2-3 seconds
- **Output size**: ~50-100 MB (all formats)

## Contributing

Found a bug? Have a suggestion?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Credits

- Python pydoc library
- Community contributors
- Based on best practices for documentation export

## Version

**Current Version:** 1.0.0  
**Last Updated:** January 2024  
**Status:** Stable

## Support

Need help?
- 📖 Read the [Full Documentation](docs/README_EN.md)
- 🐛 Check [Issues](https://github.com/example/issues)
- 💬 Start a [Discussion](https://github.com/example/discussions)

---

**Made with ❤️ for Python developers**

[⬆ back to top](#pydocsexport)
