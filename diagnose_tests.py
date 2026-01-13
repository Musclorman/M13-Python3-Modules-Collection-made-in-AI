#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Diagnostic script to identify pytest collection errors
"""

import subprocess
import sys


def main():
    """Run pytest with detailed error output"""
    print("=" * 70)
    print("Pytest Collection Diagnostic")
    print("=" * 70)
    print()
    
    # Run pytest with collection output
    cmd = [
        sys.executable, "-m", "pytest",
        "--collect-only",
        "-q",
        "--tb=long"
    ]
    
    print(f"Running: {' '.join(cmd)}")
    print()
    
    result = subprocess.run(cmd)
    
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
