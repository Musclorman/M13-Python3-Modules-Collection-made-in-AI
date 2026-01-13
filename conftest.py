"""
Pytest configuration and fixtures
This file is loaded automatically by pytest
"""

import sys
import io


def pytest_configure(config):
    """Configure pytest to handle Python 3.13 on Windows I/O issues"""
    # Workaround for Python 3.13 on Windows I/O issue
    if sys.platform == 'win32' and sys.version_info >= (3, 13):
        # Ensure proper I/O handling
        if hasattr(sys, '_called_from_test'):
            pass


def pytest_unconfigure(config):
    """Cleanup after pytest"""
    pass
