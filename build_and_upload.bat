@echo off
REM Unified Build and Upload Script for Windows
REM This script provides a menu to build, test, and upload packages to PyPI

setlocal enabledelayedexpansion
cls

:menu
echo.
echo ========================================================================
echo Build and Upload Menu - M13 Python Modules Collection
echo ========================================================================
echo.
echo Select an action:
echo   1. Build distribution package
echo   2. Run tests
echo   3. Upload to PyPI (TestPyPI)
echo   4. Upload to PyPI (Production)
echo   5. Execute all actions (build, test, upload to TestPyPI)
echo   6. Execute all actions (build, test, upload to Production)
echo   0. Quit without doing anything
echo.
set /p choice="Enter your choice (0-6): "

if "%choice%"=="0" goto quit
if "%choice%"=="1" goto build_only
if "%choice%"=="2" goto test_only
if "%choice%"=="3" goto upload_test
if "%choice%"=="4" goto upload_prod
if "%choice%"=="5" goto all_test
if "%choice%"=="6" goto all_prod

echo.
echo [ERROR] Invalid choice. Please enter a number between 0 and 6.
pause
goto menu

:build_only
echo.
echo ========================================================================
echo Building distribution package...
echo ========================================================================
call :build
if %ERRORLEVEL% EQU 0 (
    pause
) else (
    pause
)
goto menu

:test_only
echo.
echo ========================================================================
echo Running tests...
echo ========================================================================
call :test
if %ERRORLEVEL% EQU 0 (
    pause
) else (
    pause
)
goto menu

:upload_test
echo.
echo ========================================================================
echo Uploading to TestPyPI...
echo ========================================================================
call :check_dist
if %ERRORLEVEL% NEQ 0 goto menu
call :upload_testpypi
pause
goto menu

:upload_prod
echo.
echo ========================================================================
echo Uploading to Production PyPI
echo ========================================================================
call :check_dist
if %ERRORLEVEL% NEQ 0 goto menu
call :upload_pypi
pause
goto menu

:all_test
echo.
echo ========================================================================
echo Executing: Build, Test, and Upload to TestPyPI
echo ========================================================================
call :build
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Build failed. Stopping.
    pause
    goto menu
)
call :test
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [WARNING] Tests failed. Continuing with upload...
)
call :upload_testpypi
pause
goto menu

:all_prod
echo.
echo ========================================================================
echo Executing: Build, Test, and Upload to Production PyPI
echo ========================================================================
call :build
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Build failed. Stopping.
    pause
    goto menu
)
call :test
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [WARNING] Tests failed. Continuing with upload...
)
call :upload_pypi
pause
goto menu

:quit
echo.
echo [OK] Quitting without doing anything.
echo.
exit /b 0

REM ========================================================================
REM Function: Build distribution
REM ========================================================================
:build
echo.
echo 1. Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
echo    [OK] Cleaned

echo.
echo 2. Checking build dependencies...
python -c "import setuptools, wheel, build" 2>nul || (
    echo    Installing build tools...
    python -m pip install setuptools wheel build
)
echo    [OK] Dependencies OK

echo.
echo 3. Building distribution package...
python -m build
if %ERRORLEVEL% EQU 0 (
    echo    [OK] Build successful
    exit /b 0
) else (
    echo    [ERROR] Build failed
    exit /b 1
)

REM ========================================================================
REM Function: Run tests
REM ========================================================================
:test
echo.
echo 1. Checking pytest installation...
python -c "import pytest" 2>nul || (
    echo    Installing pytest...
    python -m pip install pytest
)
echo    [OK] pytest OK

echo.
echo 2. Running tests...
python run_tests.py
if %ERRORLEVEL% EQU 0 (
    echo.
    echo    [OK] Tests passed
    exit /b 0
) else (
    echo.
    echo    [WARNING] Some tests failed
    exit /b 1
)

REM ========================================================================
REM Function: Check if dist directory exists
REM ========================================================================
:check_dist
if not exist dist (
    echo.
    echo [ERROR] dist\ directory not found!
    echo   Please run 'Build distribution package' first
    exit /b 1
)
exit /b 0

REM ========================================================================
REM Function: Upload to TestPyPI
REM ========================================================================
:upload_testpypi
echo.
echo 1. Checking twine installation...
python -c "import twine" 2>nul || (
    echo    Installing twine...
    python -m pip install twine
)
echo    [OK] twine OK

echo.
echo 2. Uploading to TestPyPI...
python -m twine upload --repository testpypi dist\*
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Upload to TestPyPI successful!
    echo.
    echo Test installation with:
    echo   pip install --index-url https://test.pypi.org/simple/ M13aiCollection
) else (
    echo.
    echo [ERROR] Upload to TestPyPI failed
)
exit /b %ERRORLEVEL%

REM ========================================================================
REM Function: Upload to Production PyPI
REM ========================================================================
:upload_pypi
echo.
echo 1. Checking twine installation...
python -c "import twine" 2>nul || (
    echo    Installing twine...
    python -m pip install twine
)
echo    [OK] twine OK

echo.
echo [WARNING] PRODUCTION UPLOAD
echo   Make sure you have configured your PyPI credentials!
echo.
set /p confirm="Continue with production upload? (y/n): "

if /i not "%confirm%"=="y" (
    echo.
    echo [ERROR] Upload cancelled.
    exit /b 1
)

echo.
echo 2. Uploading to Production PyPI...
python -m twine upload dist\*
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Upload to PyPI successful!
    echo.
    echo Install with:
    echo   pip install M13aiCollection
) else (
    echo.
    echo [ERROR] Upload to PyPI failed
)
exit /b %ERRORLEVEL%
