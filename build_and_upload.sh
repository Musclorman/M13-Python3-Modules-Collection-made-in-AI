#!/bin/bash
# Unified Build and Upload Script for Linux/Mac
# This script provides a menu to build, test, and upload packages to PyPI

clear

menu() {
    while true; do
        echo ""
        echo "========================================================================"
        echo "Build and Upload Menu - M13 Python Modules Collection"
        echo "========================================================================"
        echo ""
        echo "Select an action:"
        echo "  1. Build distribution package"
        echo "  2. Run tests"
        echo "  3. Upload to PyPI (TestPyPI)"
        echo "  4. Upload to PyPI (Production)"
        echo "  5. Execute all actions (build, test, upload to TestPyPI)"
        echo "  6. Execute all actions (build, test, upload to Production)"
        echo "  0. Quit without doing anything"
        echo ""
        read -p "Enter your choice (0-6): " choice

        case $choice in
            0) quit_menu ;;
            1) build_only ;;
            2) test_only ;;
            3) upload_test ;;
            4) upload_prod ;;
            5) all_test ;;
            6) all_prod ;;
            *) 
                echo ""
                echo "✗ Invalid choice. Please enter a number between 0 and 6."
                ;;
        esac
    done
}

build_only() {
    echo ""
    echo "========================================================================"
    echo "Building distribution package..."
    echo "========================================================================"
    build_package
}

test_only() {
    echo ""
    echo "========================================================================"
    echo "Running tests..."
    echo "========================================================================"
    run_tests
}

upload_test() {
    echo ""
    echo "========================================================================"
    echo "Uploading to TestPyPI..."
    echo "========================================================================"
    check_dist || return
    upload_testpypi
}

upload_prod() {
    echo ""
    echo "========================================================================"
    echo "Uploading to Production PyPI"
    echo "========================================================================"
    check_dist || return
    upload_pypi
}

all_test() {
    echo ""
    echo "========================================================================"
    echo "Executing: Build, Test, and Upload to TestPyPI"
    echo "========================================================================"
    build_package || {
        echo ""
        echo "✗ Build failed. Stopping."
        return 1
    }
    run_tests || {
        echo ""
        echo "⚠ Tests failed. Continuing with upload..."
    }
    upload_testpypi
}

all_prod() {
    echo ""
    echo "========================================================================"
    echo "Executing: Build, Test, and Upload to Production PyPI"
    echo "========================================================================"
    build_package || {
        echo ""
        echo "✗ Build failed. Stopping."
        return 1
    }
    run_tests || {
        echo ""
        echo "⚠ Tests failed. Continuing with upload..."
    }
    upload_pypi
}

quit_menu() {
    echo ""
    echo "✓ Quitting without doing anything."
    echo ""
    exit 0
}

# ========================================================================
# Function: Build distribution
# ========================================================================
build_package() {
    echo ""
    echo "1. Cleaning previous builds..."
    rm -rf build/ dist/ *.egg-info
    echo "   ✓ Cleaned"

    echo ""
    echo "2. Checking build dependencies..."
    python3 -c "import setuptools, wheel, build" 2>/dev/null || {
        echo "   Installing build tools..."
        python3 -m pip install setuptools wheel build
    }
    echo "   ✓ Dependencies OK"

    echo ""
    echo "3. Building distribution package..."
    python3 -m build
    BUILD_STATUS=$?

    if [ $BUILD_STATUS -eq 0 ]; then
        echo "   ✓ Build successful"
        return 0
    else
        echo "   ✗ Build failed"
        return 1
    fi
}

# ========================================================================
# Function: Run tests
# ========================================================================
run_tests() {
    echo ""
    echo "1. Checking pytest installation..."
    python3 -c "import pytest" 2>/dev/null || {
        echo "   Installing pytest..."
        python3 -m pip install pytest
    }
    echo "   ✓ pytest OK"

    echo ""
    echo "2. Running tests..."
    pytest -v
    TEST_STATUS=$?

    if [ $TEST_STATUS -eq 0 ]; then
        echo ""
        echo "   ✓ Tests passed"
        return 0
    else
        echo ""
        echo "   ✗ Some tests failed"
        return 1
    fi
}

# ========================================================================
# Function: Check if dist directory exists
# ========================================================================
check_dist() {
    if [ ! -d "dist" ]; then
        echo ""
        echo "✗ dist/ directory not found!"
        echo "  Please run 'Build distribution package' first"
        return 1
    fi
    return 0
}

# ========================================================================
# Function: Upload to TestPyPI
# ========================================================================
upload_testpypi() {
    echo ""
    echo "1. Checking twine installation..."
    python3 -c "import twine" 2>/dev/null || {
        echo "   Installing twine..."
        python3 -m pip install twine
    }
    echo "   ✓ twine OK"

    echo ""
    echo "2. Uploading to TestPyPI..."
    python3 -m twine upload --repository testpypi dist/*
    UPLOAD_STATUS=$?

    if [ $UPLOAD_STATUS -eq 0 ]; then
        echo ""
        echo "✓ Upload to TestPyPI successful!"
        echo ""
        echo "Test installation with:"
        echo "  pip install --index-url https://test.pypi.org/simple/ generic-tree"
    else
        echo ""
        echo "✗ Upload to TestPyPI failed"
    fi
    return $UPLOAD_STATUS
}

# ========================================================================
# Function: Upload to Production PyPI
# ========================================================================
upload_pypi() {
    echo ""
    echo "1. Checking twine installation..."
    python3 -c "import twine" 2>/dev/null || {
        echo "   Installing twine..."
        python3 -m pip install twine
    }
    echo "   ✓ twine OK"

    echo ""
    echo "⚠ PRODUCTION UPLOAD"
    echo "  Make sure you have configured your PyPI credentials!"
    echo ""
    read -p "Continue with production upload? (y/n): " confirm

    if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
        echo ""
        echo "✗ Upload cancelled."
        return 1
    fi

    echo ""
    echo "2. Uploading to Production PyPI..."
    python3 -m twine upload dist/*
    UPLOAD_STATUS=$?

    if [ $UPLOAD_STATUS -eq 0 ]; then
        echo ""
        echo "✓ Upload to PyPI successful!"
        echo ""
        echo "Install with:"
        echo "  pip install generic-tree"
    else
        echo ""
        echo "✗ Upload to PyPI failed"
    fi
    return $UPLOAD_STATUS
}

# Start the menu
menu
