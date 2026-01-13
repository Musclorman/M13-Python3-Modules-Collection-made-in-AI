#!/bin/bash
# Upload script for Generic Tree to PyPI (Linux/Mac)

echo "========================================================================"
echo "Generic Tree - Upload to PyPI"
echo "========================================================================"

# Check if dist directory exists
if [ ! -d "dist" ]; then
    echo ""
    echo "✗ dist/ directory not found!"
    echo "  Please run './build.sh' first"
    exit 1
fi

# Check if twine is installed
echo ""
echo "Checking twine installation..."
python3 -c "import twine" 2>/dev/null || {
    echo "Installing twine..."
    python3 -m pip install twine
}

# Ask user where to upload
echo ""
echo "Upload to:"
echo "  1. TestPyPI (for testing before production)"
echo "  2. Production PyPI"
echo ""
read -p "Choose destination (1 or 2): " choice

case $choice in
    1)
        echo ""
        echo "Uploading to TestPyPI..."
        python3 -m twine upload --repository testpypi dist/*
        UPLOAD_STATUS=$?
        if [ $UPLOAD_STATUS -eq 0 ]; then
            echo ""
            echo "✓ Upload to TestPyPI successful!"
            echo "Test installation with:"
            echo "  pip install --index-url https://test.pypi.org/simple/ generic-tree"
        fi
        ;;
    2)
        echo ""
        echo "⚠ Uploading to production PyPI"
        echo "   Make sure you have configured your PyPI credentials!"
        echo ""
        read -p "Continue? (y/n): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            python3 -m twine upload dist/*
            UPLOAD_STATUS=$?
            if [ $UPLOAD_STATUS -eq 0 ]; then
                echo ""
                echo "✓ Upload to PyPI successful!"
                echo "Install with:"
                echo "  pip install generic-tree"
            fi
        fi
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

exit $UPLOAD_STATUS
