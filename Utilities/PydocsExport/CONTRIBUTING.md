# Contributing to PydocsExport

First off, thanks for taking the time to contribute! 🎉

The following is a set of guidelines for contributing to PydocsExport.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct.
By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out
that you don't need to create one. When you are creating a bug report, please
include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement
suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python styleguide
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Styleguide

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Python Styleguide

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose
- Use type hints where appropriate

Example:

```python
def export_documentation(
    format: str,
    output_path: str = "output"
) -> Dict[str, Any]:
    """
    Export documentation in specified format.
    
    Args:
        format: Export format (txt, pdf, epub, mobi, html)
        output_path: Path where to save files
        
    Returns:
        Dictionary with export results
    """
    pass
```

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help organize and categorize issues and
pull requests.

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## Recognition

Contributors will be recognized in:
- The README.md file
- Release notes
- GitHub contributors page

Thank you for contributing to PydocsExport! 🚀
