## 🚀 QUICK START GUIDE - PydocsExport

### Installation (30 seconds)

```bash
# No installation needed! Just run:
python EasyPydocsExport.py --help
```

### Basic Usage (1 minute)

```bash
# Export everything to default folder
python EasyPydocsExport.py

# Export only what you need
python EasyPydocsExport.py --txt --html

# Save to custom location
python EasyPydocsExport.py --output C:\my\docs
```

### Common Commands

| What you want | Command |
|---|---|
| All formats | `python EasyPydocsExport.py` |
| Text only | `python EasyPydocsExport.py --txt` |
| PDFs only | `python EasyPydocsExport.py --pdf` |
| E-books only | `python EasyPydocsExport.py --epub --mobi` |
| HTML only | `python EasyPydocsExport.py --html` |
| Custom folder | `python EasyPydocsExport.py --output D:\docs` |

### What You Get

After export, check these folders:
- `TXT/` - Text files with chapters
- `PDF/` - PDFs for different paper sizes (A0, A1, A3, A4, etc.)
- `EBOOK_EPUB/` - For iPad, Kobo, e-readers
- `EBOOK_MOBI/` - For Kindle
- `HTML/` - Interactive web pages
- `INDEX.txt` - Summary of everything
- `export_log_*.json` - Details of what was exported

### Using in Python Code

```python
from src.exporter import PydocsExporter

# Create exporter
exporter = PydocsExporter()

# Export
results = exporter.export_all(['txt', 'epub'])

print(f"✓ Exported {results['total_modules']} modules")
```

### Run Tests

```bash
python tests/test_pydocs_export.py
```

### Troubleshooting

**"Module not found" error?**
→ Make sure you're in the PydocsExport folder

**"Permission denied"?**
→ Use `--output` to save to a writable location

**Export is slow?**
→ It's normal for first export. Just wait!

---

## 📖 Full Documentation

- **English**: `docs/README_EN.md`
- **Français**: `docs/README_FR.md`
- **Español**: `docs/README_ES.md`
- **Deutsch**: `docs/README_DE.md`
- **Italiano**: `docs/README_IT.md`

---

## Features at a Glance

✨ **5 Formats** - TXT, PDF, EPUB, MOBI, HTML

📄 **Smart Organization** - Automatic chapters & indexes

🌍 **Multilingual** - 5 languages supported

📊 **Detailed Logs** - Track what was exported

🚀 **Zero Dependencies** - Just Python, nothing else

---

**Questions?** Check the README.md or full documentation files.

**Ready to export?** Run: `python EasyPydocsExport.py`

---

Created with ❤️ for Python lovers everywhere! 🐍
