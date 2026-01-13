#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build script for Generic Tree package (cross-platform).

This script builds the distribution package for PyPI
"""

import subprocess
import sys
import os
from pathlib import Path


def main():
    """Main build function"""
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("=" * 70)
    print("Generic Tree - Build Script")
    print("=" * 70)
    
    # Check if setuptools and wheel are installed
    print("\n1. Checking dependencies...")
    try:
        __import__("setuptools")
        __import__("wheel")
        print("   [OK] setuptools installed")
        print("   [OK] wheel installed")
    except ImportError as e:
        print(f"   [ERROR] Missing dependency: {e}")
        print("   Installing build tools...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install",
             "setuptools", "wheel", "build"]
        )
    
    # Clean previous builds
    print("\n2. Cleaning previous builds...")
    if Path("build").exists():
        import shutil
        shutil.rmtree("build")
        print("   [OK] Removed build directory")
    if Path("dist").exists():
        import shutil
        shutil.rmtree("dist")
        print("   [OK] Removed dist directory")
    
    # Build the package
    print("\n3. Building distribution package...")
    try:
        subprocess.check_call([sys.executable, "-m", "build"])
        print("   [OK] Build successful")
    except subprocess.CalledProcessError as e:
        print(f"   [ERROR] Build failed: {e}")
        return 1
    
    # Verify the build
    print("\n4. Verifying build...")
    if Path("dist").exists():
        files = list(Path("dist").glob("*"))
        print(f"   [OK] Build created {len(files)} file(s):")
        for f in files:
            print(f"     - {f.name}")
    else:
        print("   [ERROR] Build verification failed")
        return 1
    
    print("\n" + "=" * 70)
    print("Build completed successfully!")
    print("=" * 70)
    print("\nNext steps:")
    print("  1. Verify package: python -m twine check dist/*")
    print("  2. Upload to PyPI: python -m twine upload dist/*")
    print("  3. Or run: build_and_upload.sh (Linux/Mac) or "
          "build_and_upload.bat (Windows)")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
