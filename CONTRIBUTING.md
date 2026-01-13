# Contributing to Generic Tree

Thank you for your interest in contributing to Generic Tree! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful and constructive. All contributors are expected to maintain a professional and inclusive environment.

## Reporting Bugs

When reporting bugs, please include:

- **Title**: Clear, descriptive title
- **Environment**: Python version, OS, package version
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Code Example**: Minimal code that demonstrates the bug
- **Traceback**: Full error traceback if applicable

Example:
```
Title: Tree.traverse() fails with empty tree

Python: 3.9
OS: Windows 10
Package: generic-tree 1.0.0

Steps:
1. Create empty tree
2. Call traverse()

Expected: Returns empty iterator
Actual: Raises AttributeError
```

## Suggesting Enhancements

When suggesting enhancements:

- Describe the current behavior
- Describe the desired behavior
- Explain why this enhancement would be useful
- Include code examples if possible
- List similar features in other libraries

## Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
4. Run tests:
   ```bash
   pytest
   ```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use type hints for all functions
- Write docstrings for all public methods
- Maximum line length: 100 characters
- Use Black for code formatting:
  ```bash
  black .
  ```
- Use isort for import sorting:
  ```bash
  isort .
  ```

## Testing

- Write tests for all new features
- Ensure all existing tests pass
- Run tests with:
  ```bash
  pytest -v
  ```
- Check coverage:
  ```bash
  pytest --cov=generic_tree
  ```

## Pull Request Process

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes with good commit messages
3. Add/update tests as needed
4. Update documentation if needed
5. Format your code:
   ```bash
   black .
   isort .
   ```
6. Run tests to ensure everything passes
7. Push your branch and create a Pull Request

In your PR description, include:
- Description of changes
- References to related issues
- Testing performed
- Any breaking changes

## Documentation

- Update docstrings using Google style
- Include type hints
- Add examples for complex features
- Update README.md if needed
- Update CHANGELOG.md with your changes

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue with the `question` label.

Thank you for contributing!
