# 🚀 HOW TO START

## In 3 Steps (30 seconds):

### Step 1: Open Terminal/Command Prompt
```bash
cd PydocsExport
```

### Step 2: Run the Export
```bash
python EasyPydocsExport.py
```

### Step 3: Check Results
Open the `pydocs_export_output/` folder that was created.

You'll find:
- **TXT/** - Text files organized by chapter
- **PDF/** - PDFs in all 11 paper sizes (A0-A10)
- **EBOOK_EPUB/** - For iPad, Kobo, etc.
- **EBOOK_MOBI/** - For Kindle
- **HTML/** - Interactive web pages

---

## Common Commands:

```bash
# Export specific formats
python EasyPydocsExport.py --txt --html

# PDF only
python EasyPydocsExport.py --pdf

# Custom output directory
python EasyPydocsExport.py --output C:\my\docs

# Show all options
python EasyPydocsExport.py --help
```

---

## Run Tests:
```bash
python tests/test_pydocs_export.py
```

## View Examples:
```bash
python examples.py
```

---

## Files to Read:

1. **README.md** - Project overview
2. **QUICKSTART.md** - Quick reference
3. **docs/README_EN.md** - Complete documentation

Enjoy! 📚✨
