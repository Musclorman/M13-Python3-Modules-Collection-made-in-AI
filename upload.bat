@echo off
REM Upload script for Generic Tree to PyPI (Windows)

echo ========================================================================
echo Generic Tree - Upload to PyPI
echo ========================================================================

REM Check if dist directory exists
if not exist dist (
    echo.
    echo ✗ dist\ directory not found!
    echo   Please run 'build.bat' first
    exit /b 1
)

REM Check if twine is installed
echo.
echo Checking twine installation...
python -c "import twine" 2>nul || (
    echo Installing twine...
    python -m pip install twine
)

REM Ask user where to upload
echo.
echo Upload to:
echo   1. TestPyPI (for testing before production)
echo   2. Production PyPI
echo.
set /p choice="Choose destination (1 or 2): "

if "%choice%"=="1" (
    echo.
    echo Uploading to TestPyPI...
    python -m twine upload --repository testpypi dist\*
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo ✓ Upload to TestPyPI successful!
        echo Test installation with:
        echo   pip install --index-url https://test.pypi.org/simple/ generic-tree
    )
) else if "%choice%"=="2" (
    echo.
    echo ⚠ Uploading to production PyPI
    echo    Make sure you have configured your PyPI credentials!
    echo.
    set /p confirm="Continue? (y/n): "
    if /i "%confirm%"=="y" (
        python -m twine upload dist\*
        if %ERRORLEVEL% EQU 0 (
            echo.
            echo ✓ Upload to PyPI successful!
            echo Install with:
            echo   pip install generic-tree
        )
    )
) else (
    echo Invalid choice
    exit /b 1
)
