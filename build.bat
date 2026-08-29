@echo off
echo ========================================
echo   Snake Game - Build to EXE
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Checking dependencies...
pip show pygame >nul 2>&1
if errorlevel 1 (
    echo Installing pygame...
    pip install pygame
)

pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing pyinstaller...
    pip install pyinstaller
)

echo.
echo Building executable...
echo ========================================
pyinstaller --onefile --windowed --name=SnakeGame snake_game.py

if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! EXE file created!
echo ========================================
echo.
echo EXE location: %cd%\dist\SnakeGame.exe
echo.
pause