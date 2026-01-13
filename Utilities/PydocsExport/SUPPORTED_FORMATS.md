# Supported Formats Guide

## Quick Reference

### Export All Formats
```bash
python EasyPydocsExport.py --all
```

### Export by Format Type

#### Document Formats
```bash
python EasyPydocsExport.py --pdf --docx
```

#### eBook Formats
```bash
python EasyPydocsExport.py --epub --mobi --azw
```

#### Markup/Documentation Formats
```bash
python EasyPydocsExport.py --md --rst
```

#### Data/Structured Formats
```bash
python EasyPydocsExport.py --xml --json --yaml --csv --sqlite
```

#### All Text-Based Formats
```bash
python EasyPydocsExport.py --txt --md --rst --html
```

---

## Format Details

### 1. TXT - Plain Text
- **Best For**: Archival, universal compatibility
- **Features**: Simple, widely compatible
- **Size**: Smallest of all formats
- **Use When**: You need maximum compatibility

### 2. PDF - Portable Document Format
- **Best For**: Professional documents, printing
- **Features**: Multiple paper sizes (A0-A10)
- **Use When**: Sharing with non-technical users

### 3. HTML - HyperText Markup Language
- **Best For**: Web integration, online viewing
- **Features**: Styled with CSS, interactive
- **Use When**: Hosting on websites

### 4. Markdown (.md)
- **Best For**: GitHub, documentation repos
- **Features**: Clean syntax, easy to edit
- **Use When**: Version controlling documentation

### 5. reStructuredText (.rst)
- **Best For**: Sphinx projects, Python docs
- **Features**: Sphinx-compatible structure
- **Use When**: Using Sphinx for documentation

### 6. RTF - Rich Text Format
- **Best For**: Word processors
- **Features**: Formatted text with styling
- **Use When**: Need simple rich text format

### 7. XML - eXtensible Markup Language
- **Best For**: Data interchange, parsing
- **Features**: Structured data, parseable
- **Use When**: Need machine-readable format

### 8. JSON - JavaScript Object Notation
- **Best For**: APIs, web applications
- **Features**: Lightweight, widely supported
- **Use When**: Integrating with web services

### 9. CSV - Comma-Separated Values
- **Best For**: Spreadsheets, data analysis
- **Features**: Excel/Calc compatible
- **Use When**: Using with data tools

### 10. YAML - YAML Ain't Markup Language
- **Best For**: Configuration, readability
- **Features**: Human-friendly syntax
- **Use When**: Need human-readable data

### 11. SQLite - Database
- **Best For**: Programmatic access, queries
- **Features**: Full SQL support
- **Use When**: Need to query documentation

### 12. HLP - Windows Help Format
- **Best For**: Windows help integration
- **Features**: RTF-based structure
- **Use When**: Building help files

### 13. EPUB - Electronic Publication
- **Best For**: eBook readers, tablets
- **Features**: Standard eBook format
- **Use When**: Distribution on ereaders

### 14. MOBI - Mobipocket Format
- **Best For**: Older Kindle devices
- **Features**: Kindle compatibility
- **Use When**: Supporting legacy Kindle

### 15. AZW - Amazon eBook Format
- **Best For**: Modern Kindle devices
- **Features**: Latest Amazon format
- **Use When**: Kindle ecosystem

### 16. DOCX - Microsoft Word Format
- **Best For**: Office compatibility
- **Features**: Modern Office format
- **Use When**: MS Office integration

---

## Choosing the Right Format

### For Maximum Compatibility
```
Use: TXT, HTML, PDF
```

### For Web/Online Publishing
```
Use: HTML, Markdown, JSON
```

### For eBook Reading
```
Use: EPUB (modern), AZW (Kindle), MOBI (older Kindle)
```

### For Data Analysis
```
Use: CSV, JSON, SQLite, YAML
```

### For Technical Documentation
```
Use: Markdown, reStructuredText, HTML
```

### For Version Control (Git)
```
Use: Markdown, reStructuredText, CSV
```

### For Information Exchange
```
Use: JSON, XML, YAML
```

### For Database Integration
```
Use: SQLite, CSV, JSON
```

---

## Output Directory Structure

```
pydocs_export_output/
├── TXT/                    # Plain text files
├── PDF/                    # PDF documents
├── HTML/                   # Web pages
├── MARKDOWN/               # .md files
├── RESTRUCTUREDTEXT/       # .rst files
├── RTF/                    # Rich text format
├── XML/                    # XML data
├── JSON/                   # JSON data
├── CSV/                    # Spreadsheet data
├── YAML/                   # YAML configuration
├── SQLITE/                 # Database files
├── HLP/                    # Windows help format
├── EBOOK_EPUB/             # EPUB eBooks
├── EBOOK_MOBI/             # MOBI eBooks
├── AZW/                    # Kindle eBooks
├── DOCX/                   # Word documents
├── INDEX.txt               # Main index
└── export_log_*.json       # Export statistics
```

---

## Format Selection by Use Case

| Use Case | Recommended Formats |
|----------|----------------------|
| Team Documentation | Markdown, HTML, PDF |
| Personal Reference | TXT, PDF |
| Web Publishing | HTML, JSON |
| eBook Creation | EPUB, AZW |
| Data Analysis | CSV, SQLite, JSON |
| Configuration | YAML, JSON |
| Archival | TXT, PDF, RTF |
| API Integration | JSON, XML |
| Sphinx Projects | reStructuredText |
| Microsoft Integration | DOCX, PDF |

---

## Performance Notes

### Fastest Exports
1. TXT (Plain text - minimal processing)
2. CSV (Tabular - simple format)
3. JSON (Lightweight format)

### Largest File Sizes
1. PDF (A0 size - multiple modules)
2. HTML (With styling)
3. DOCX (XML overhead)

### Best for Batch Operations
1. SQLite (Single database file)
2. CSV (Easy concatenation)
3. JSON (Mergeable arrays)

---

## Tips & Tricks

### Generate Only What You Need
```bash
# Don't export everything - choose specific formats
python EasyPydocsExport.py --json --csv
# Instead of: --all
```

### Combine Formats for Different Audiences
```bash
# For technical users: Markdown + JSON
python EasyPydocsExport.py --md --json

# For general users: PDF + HTML
python EasyPydocsExport.py --pdf --html

# For data scientists: CSV + SQLite
python EasyPydocsExport.py --csv --sqlite
```

### Use Python API for Automation
```python
from PydocsExport import export_data_formats, export_ebook_formats

# Export data formats for processing
export_data_formats()

# Export for reading
export_ebook_formats()
```

---

## Format Compatibility Matrix

| Format | Windows | macOS | Linux | Web | Mobile | Offline |
|--------|---------|-------|-------|-----|--------|---------|
| TXT | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PDF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| HTML | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Markdown | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| RST | ✓ | ✓ | ✓ | ✓ | ~ | ✓ |
| JSON | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| CSV | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| XML | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| YAML | ✓ | ✓ | ✓ | ✓ | ~ | ✓ |
| SQLite | ✓ | ✓ | ✓ | ~ | ~ | ✓ |
| EPUB | ✓ | ✓ | ✓ | ~ | ✓ | ✓ |
| MOBI | ✓ | ✓ | ✓ | ~ | ✓ | ✓ |
| AZW | ✓ | ✓ | ✓ | ~ | ✓ | ✓ |
| DOCX | ✓ | ✓ | ✓ | ~ | ✓ | ✓ |
| RTF | ✓ | ✓ | ✓ | ~ | ~ | ✓ |
| HLP | ✓ | ~ | ~ | ~ | ~ | ✓ |

**Legend**: ✓ Full Support | ~ Partial Support | - No Support

---

Generated with **PydocsExport v1.1.1**
