#!/bin/bash
# Build script for Generic Tree package (Linux/Mac)

echo "========================================================================"
echo "Generic Tree - Build Script (Linux/Mac)"
echo "========================================================================"

# Clean previous builds
echo ""
echo "1. Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info
echo "   ✓ Cleaned"

# Install build tools if needed
echo ""
echo "2. Checking dependencies..."
python3 -c "import setuptools, wheel, build" 2>/dev/null || {
    echo "   Installing build tools..."
    python3 -m pip install setuptools wheel build
}
echo "   ✓ Dependencies OK"

# Build the package
echo ""
echo "3. Building distribution package..."
python3 -m build
BUILD_STATUS=$?

if [ $BUILD_STATUS -eq 0 ]; then
    echo "   ✓ Build successful"
    echo ""
    echo "========================================================================"
    echo "Build completed successfully!"
    echo "========================================================================"
    echo ""
    echo "Next steps:"
    echo "  1. Verify: python3 -m twine check dist/*"
    echo "  2. Upload: python3 -m twine upload dist/*"
    echo "  3. Or use: ./upload.sh"
else
    echo "   ✗ Build failed"
    exit 1
fi
