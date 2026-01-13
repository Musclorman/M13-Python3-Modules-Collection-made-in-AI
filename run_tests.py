#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test runner script - Workaround for pytest I/O issues on Windows/Python 3.13
Uses pytest but with environment variables to avoid I/O problems
"""

import subprocess
import sys
import os


def main():
    """Run tests with environment variables to avoid I/O issues"""
    
    # Set environment variables for proper I/O handling
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    
    # Construct pytest command
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    # If no arguments provided, run with sensible defaults
    if not args:
        args = ['-v', '--tb=short']
    
    cmd = [sys.executable, '-m', 'pytest'] + args
    
    print("=" * 70)
    print(f"Running: {' '.join(cmd)}")
    print("=" * 70)
    print()
    
    try:
        # Run pytest with modified environment
        process = subprocess.Popen(
            cmd,
            env=env,
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True
        )
        
        # Wait for completion
        returncode = process.wait()
        
        return returncode
        
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"Error running tests: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
