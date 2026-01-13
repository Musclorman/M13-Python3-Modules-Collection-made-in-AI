#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Diagnostic script to check build issues."""

import subprocess
import sys
import os

def check_imports():
    """Check if main modules can be imported."""
    print("Checking imports...")
    try:
        from VariableExtender.generic_tree import Tree
        print("[OK] VariableExtender.generic_tree.Tree")
    except Exception as e:
        print(f"[ERROR] VariableExtender.generic_tree: {e}")
        return False
    
    try:
        from VariableExtender.MenuMaker import menu
        print("[OK] VariableExtender.MenuMaker.menu")
    except Exception as e:
        print(f"[ERROR] VariableExtender.MenuMaker: {e}")
        return False
    
    return True


def check_build():
    """Check if build works."""
    print("\nChecking build...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "build"],
            cwd=os.getcwd(),
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print("[OK] Build succeeded")
            return True
        else:
            print(f"[ERROR] Build failed with code {result.returncode}")
            if result.stdout:
                print("STDOUT:")
                print(result.stdout[:1000])
            if result.stderr:
                print("STDERR:")
                print(result.stderr[:1000])
            return False
    except subprocess.TimeoutExpired:
        print("[ERROR] Build timeout")
        return False
    except Exception as e:
        print(f"[ERROR] Build error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 70)
    print("Build Diagnostic")
    print("=" * 70)
    
    check_imports()
    check_build()
