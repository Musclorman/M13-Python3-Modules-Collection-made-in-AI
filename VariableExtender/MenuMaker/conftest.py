"""Pytest configuration for MenuMaker tests."""

import sys
from pathlib import Path

# Add the module directory to the path
module_dir = Path(__file__).parent
sys.path.insert(0, str(module_dir))
