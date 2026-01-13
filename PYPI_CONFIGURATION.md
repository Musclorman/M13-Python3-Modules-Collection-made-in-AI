# PyPI Configuration Instructions

## 📋 Package Information

```
Package Name: variableplus
Version: 0.1
Author: Musclor13
License: MIT
Python: >= 3.7
Repository: https://github.com/Musclor13/variableplus
```

---

## 🔐 PyPI Credentials Setup

### For Windows Users

#### Step 1: Create ~/.pypirc

Go to your user home directory:
```
C:\Users\[YourUsername]\
```

Create a file named `.pypirc` with content:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi_YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

#### Step 2: Get Your API Token

1. Go to https://pypi.org/account/
2. Log in with your PyPI account
3. Scroll to "API tokens"
4. Click "Create token"
5. Name it "variableplus" or similar
6. Copy the entire token (starts with "pypi_")
7. Paste into `.pypirc` file

#### Step 3: Permissions

Set file permissions (PowerShell as Admin):
```powershell
# Set read-only for user
icacls "C:\Users\[YourUsername]\.pypirc" /inheritance:r /grant:r "$env:USERNAME:(R)"
```

### For Linux/Mac Users

Create `~/.pypirc`:
```bash
nano ~/.pypirc
```

Same content as above, then:
```bash
chmod 600 ~/.pypirc
```

---

## 🧪 Environment Variables (Optional)

You can also use environment variables instead of .pypirc:

### Windows PowerShell
```powershell
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = "pypi_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
$env:TWINE_REPOSITORY = "pypi"
```

### Windows Command Prompt
```cmd
set TWINE_USERNAME=__token__
set TWINE_PASSWORD=pypi_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWINE_REPOSITORY=pypi
```

### Linux/Mac
```bash
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="pypi_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
export TWINE_REPOSITORY="pypi"
```

---

## 📦 Package Configuration

### setup.py Settings

Already configured for:
- Package: `variableplus`
- Author: `Musclor13`
- Version: `1.0.0`
- License: `MIT`
- Python: `>=3.7`

### pyproject.toml Settings

Already configured for:
- Project: `variableplus`
- Author: `Musclor13`
- Description: Full package collection
- Keywords: 12 relevant keywords
- Classifiers: 44 PyPI classifiers

---

## ✅ Verification

### Before Publishing

```bash
# Check configuration
python -m build --help

# Validate metadata
twine check dist/*

# Test on TestPyPI
twine upload --repository testpypi dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ variableplus
```

### Publishing Command

```bash
# Upload to PyPI
twine upload dist/*
```

---

## 🐍 Python Package Index

### Production PyPI
- URL: https://pypi.org/
- Package URL: https://pypi.org/project/variableplus/

### Test PyPI
- URL: https://test.pypi.org/
- Test Package: https://test.pypi.org/project/variableplus/

---

## 🔄 Version Management

For future releases:

1. Update version in:
   - `setup.py` → `version='1.1.0'`
   - `pyproject.toml` → `version = "1.1.0"`
   - Root `__init__.py` if version is stored there

2. Update `CHANGELOG.md` with changes

3. Build and upload:
   ```bash
   python -m build
   twine upload dist/*
   ```

---

## 📊 Classifiers Reference

Your package includes these classifiers:

**Development Status**
- `Development Status :: 5 - Production/Stable`

**Audience**
- `Intended Audience :: Developers`
- `Intended Audience :: Education`

**Topics**
- `Topic :: Software Development :: Libraries :: Python Modules`
- `Topic :: Utilities`
- `Topic :: Software Development`

**License**
- `License :: OSI Approved :: MIT License`

**Python Versions**
- `Programming Language :: Python :: 3`
- `Programming Language :: Python :: 3.7` through `3.13`

**Operating System**
- `Operating System :: OS Independent`

**Languages**
- `Natural Language :: English`
- `Natural Language :: French`
- `Natural Language :: Spanish`
- `Natural Language :: German`
- `Natural Language :: Italian`
- `Natural Language :: Chinese (Simplified)`

---

## 🎯 Keywords

Your package includes these 12 keywords:

```
tree, data-structure, n-ary, menu, interface, 
multidimensional, array, geometry, shapes, 
algorithm, collection, package
```

---

## 📝 Files Summary

| File | Purpose |
|------|---------|
| README.md | Main documentation (Bilingual) |
| setup.py | Classic packaging configuration |
| pyproject.toml | Modern packaging configuration |
| CHANGELOG.md | Version history |
| CONTRIBUTING.md | Contribution guidelines |
| LICENSE | MIT License |

---

## ✨ Important Notes

1. **API Token**: Use `__token__` as username (not email)
2. **Token Security**: Keep your token secret, don't commit to git
3. **Two-Factor Auth**: Enable on PyPI for security
4. **.gitignore**: Make sure `.pypirc` is in `.gitignore`
5. **Version Uniqueness**: Each version can only be uploaded once
6. **Naming**: Package name must be unique on PyPI

---

## 🔗 Useful Commands

```bash
# Build package
python -m build

# Check metadata
twine check dist/*

# List contents
tar -tzf dist/variableplus-1.0.0.tar.gz

# Test on TestPyPI
twine upload --repository testpypi dist/* --verbose

# Upload to PyPI
twine upload dist/*

# Install from PyPI
pip install variableplus

# Install specific version
pip install variableplus==1.0.0

# Upgrade
pip install --upgrade variableplus

# Uninstall
pip uninstall variableplus

# Check installed version
pip show variableplus
```

---

## 🆘 Troubleshooting

### Token Not Working
- Go to https://pypi.org/account/
- Check token expiration date
- Regenerate token if needed
- Verify token in `.pypirc` file

### Package Name Already Taken
- Package names must be unique
- Try different name on PyPI
- Update `setup.py` and `pyproject.toml`

### Version Already Uploaded
- Each version can only be uploaded once
- Increment version in `setup.py` and `pyproject.toml`
- Rebuild and upload again

### File Already Exists
- Similar issue as version already uploaded
- Clean `dist/` folder
- Rebuild with new version
- Upload again

---

## 📚 Resources

- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [setuptools Guide](https://setuptools.pypa.io/)
- [Python Packaging](https://packaging.python.org/)
- [PEP 427 - Wheel](https://www.python.org/dev/peps/pep-0427/)
- [PEP 518 - pyproject.toml](https://www.python.org/dev/peps/pep-0518/)

---

**Ready to publish!** 🚀

For detailed publication instructions, see `PYPI_PUBLICATION_GUIDE.md`

---

**Created**: January 13, 2026  
**By**: Musclor13 (with AI assistance)  
**License**: MIT
