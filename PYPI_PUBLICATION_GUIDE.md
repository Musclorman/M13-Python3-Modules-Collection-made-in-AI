# PyPI Publication Guide - variableplus

**Date**: January 13, 2026  
**Package**: variableplus  
**Author**: Musclor13  
**Status**: Ready for Publication  

---

## 📋 Pre-Publication Checklist

Before publishing to PyPI, verify:

- ✅ Package name: `variableplus`
- ✅ Author: `Musclor13`
- ✅ Version: `1.0.0`
- ✅ License: MIT
- ✅ README: Bilingual (EN/FR)
- ✅ Configuration: setup.py and pyproject.toml updated
- ✅ Metadata: Consistent across all files
- ✅ No email addresses exposed
- ✅ All modules included (4 modules)
- ✅ Type hints present
- ✅ Tests included

---

## 🚀 Step 1: Prepare Your Environment

### Install Build Tools

```bash
pip install --upgrade pip setuptools wheel
pip install build twine
```

### Create PyPI Account (if needed)

1. Visit https://pypi.org/account/register/
2. Create your account
3. Enable 2FA (recommended)

---

## 🔐 Step 2: Configure PyPI Credentials

### Method A: Using API Token (Recommended)

1. Go to PyPI account settings: https://pypi.org/account/
2. Create an API token
3. Create or update `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi_YOUR_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi_YOUR_TOKEN_HERE
```

### Method B: Using Username/Password

```ini
[pypi]
username = your_username
password = your_password
```

### Windows Note

Place `.pypirc` in `%APPDATA%` or `~` (user home directory).

---

## 🏗️ Step 3: Build the Package

### From Project Root

```bash
# Navigate to project directory
cd c:\Users\Musclor13\Documents\PYTHON\variableplus

# Build distributions
python -m build
```

This creates:
- `dist/variableplus-1.0.0-py3-none-any.whl` (wheel)
- `dist/variableplus-1.0.0.tar.gz` (source)

### Verify Build

```bash
# Check contents
tar -tzf dist/variableplus-1.0.0.tar.gz | head -20
unzip -l dist/variableplus-1.0.0-py3-none-any.whl | head -20
```

---

## 🧪 Step 4: Test on TestPyPI

### Upload to TestPyPI

```bash
twine upload --repository testpypi dist/*
```

### Install from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ variableplus
```

### Verify Installation

```bash
python -c "import variableplus; print(variableplus.__version__)"
```

### Test Imports

```bash
python << EOF
from generic_tree import Tree
from MenuMaker import Menu
from Multidimention_table import MultiDimTable
from Multidimention_table.multidimention_paint import Point

print("✓ All modules imported successfully")
EOF
```

---

## 🎯 Step 5: Final Verification

### Check Package Metadata

```bash
twine check dist/*
```

Output should show:
```
Checking distribution dist/variableplus-1.0.0-py3-none-any.whl: PASSED
Checking distribution dist/variableplus-1.0.0.tar.gz: PASSED
```

### Validate Project

```bash
python validate_pypi_readiness.py
```

Expected output:
```
STATUS: SUCCESS - Ready for PyPI
```

---

## 📤 Step 6: Publish to PyPI

### Upload to PyPI

```bash
twine upload dist/*
```

### Verify Publication

```bash
# Visit package page
# https://pypi.org/project/variableplus/
```

---

## ✅ Step 7: Post-Publication Tasks

### Install from PyPI

```bash
pip install variableplus
```

### Verify Installation

```bash
python << EOF
import variableplus
print(f"✓ variableplus {variableplus.__version__} installed successfully")
print(f"✓ Location: {variableplus.__file__}")

# Test all modules
from generic_tree import Tree
from MenuMaker import Menu
from Multidimention_table import MultiDimTable
from Multidimention_table.multidimention_paint import Point

print("✓ All modules available")
EOF
```

### Update Documentation

1. Update GitHub repository:
   ```bash
   git tag v1.0.0
   git push origin main --tags
   ```

2. Create GitHub Release

3. Update README with PyPI badge (optional):
   ```markdown
   [![PyPI](https://img.shields.io/pypi/v/variableplus)](https://pypi.org/project/variableplus/)
   ```

---

## 🔄 Troubleshooting

### Error: "File already exists"

This means the version already exists on PyPI. You must increment the version:

```bash
# Update version in:
# - setup.py
# - pyproject.toml
# - __init__.py files

# Then rebuild
python -m build

# Upload again
twine upload dist/*
```

### Error: "Authentication failed"

- Verify PyPI credentials in `~/.pypirc`
- Check API token expiration
- For Windows, verify file location is correct

### Error: "Invalid distribution"

```bash
# Check for issues
twine check dist/*

# Common issues:
# - Missing long_description
# - Invalid metadata
# - Wrong file format
```

---

## 📝 Version Management

### For Next Release

1. Update version in `setup.py`:
   ```python
   version='1.1.0'
   ```

2. Update version in `pyproject.toml`:
   ```toml
   version = "1.1.0"
   ```

3. Update CHANGELOG.md with changes

4. Rebuild and upload:
   ```bash
   python -m build
   twine upload dist/*
   ```

---

## 🔗 Useful Links

### PyPI Resources
- [PyPI Official](https://pypi.org/)
- [Upload Your Project](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [setuptools Documentation](https://setuptools.pypa.io/)

### Testing
- [TestPyPI](https://test.pypi.org/)
- [Building Packages](https://packaging.python.org/tutorials/packaging-projects/)

### Badges
- [PyPI Version Badge](https://img.shields.io/pypi/v/variableplus)
- [Python Version Badge](https://img.shields.io/pypi/pyversions/variableplus)
- [License Badge](https://img.shields.io/badge/license-MIT-green)

---

## 📊 Package Statistics

### Current Package Info

| Property | Value |
|----------|-------|
| **Name** | variableplus |
| **Version** | 1.0.0 |
| **Author** | Musclor13 |
| **License** | MIT |
| **Python** | >=3.7 |
| **Modules** | 4 (generic_tree, MenuMaker, Multidimention_table, multidimention_paint) |
| **Tests** | 52+ unit tests |
| **Documentation** | 7 languages |
| **Dependencies** | 0 (zero external dependencies) |

---

## 🎓 Quick Reference

### Common Commands

```bash
# Build
python -m build

# Check
twine check dist/*

# Test upload
twine upload --repository testpypi dist/*

# Production upload
twine upload dist/*

# Install from PyPI
pip install variableplus

# Install specific version
pip install variableplus==1.0.0

# Upgrade
pip install --upgrade variableplus

# Uninstall
pip uninstall variableplus
```

---

## 📞 Support

For questions or issues during publication:

1. Check [PyPI Help](https://pypi.org/help/)
2. Read [Twine Documentation](https://twine.readthedocs.io/)
3. Check [Python Packaging Guide](https://packaging.python.org/)
4. Visit [Stack Overflow](https://stackoverflow.com/questions/tagged/pypi)

---

## ✨ After Publication

Celebrate! Your package is now available to the Python community via:

```bash
pip install variableplus
```

### Share Your Success

- Tweet about it
- Add to Python package registries
- Include in project portfolio
- Update GitHub profile

### Maintenance

- Monitor package statistics
- Respond to issues
- Release updates
- Maintain documentation

---

**Ready to publish!** 🚀

Follow the steps above in order. For support, refer to the troubleshooting section or the official PyPI documentation.

**Created**: January 13, 2026  
**By**: Musclor13 (with AI assistance)  
**License**: MIT
