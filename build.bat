@echo off
REM Build script for Generic Tree package (Windows)

echo ========================================================================
echo Generic Tree - Build Script (Windows)
echo ========================================================================

REM Clean previous builds
echo.
echo 1. Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
echo    ✓ Cleaned

REM Install build tools if needed
echo.
echo 2. Checking dependencies...
python -c "import setuptools, wheel, build" 2>nul || (
    echo    Installing build tools...
    python -m pip install setuptools wheel build
)
echo    ✓ Dependencies OK

REM Build the package
echo.
echo 3. Building distribution package...
python -m build
if %ERRORLEVEL% EQU 0 (
    echo    ✓ Build successful
    echo.
    echo ========================================================================
    echo Build completed successfully!
    echo ========================================================================
    echo.
    echo Next steps:
    echo   1. Verify: python -m twine check dist\*
    echo   2. Upload: python -m twine upload dist\*
    echo   3. Or use: upload.bat
) else (
    echo    ✗ Build failed
    exit /b 1
)
