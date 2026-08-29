#!/bin/bash
echo "========================================"
echo "  Snake Game - Build to EXE"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    exit 1
fi

echo "Checking dependencies..."
pip3 show pygame > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing pygame..."
    pip3 install pygame
fi

pip3 show pyinstaller > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing pyinstaller..."
    pip3 install pyinstaller
fi

echo ""
echo "Building executable..."
echo "========================================"
pyinstaller --onefile --windowed --name=SnakeGame snake_game.py

if [ $? -ne 0 ]; then
    echo "ERROR: Build failed!"
    exit 1
fi

echo ""
echo "========================================"
echo "SUCCESS! EXE file created!"
echo "========================================"
echo ""
echo "EXE location: $(pwd)/dist/SnakeGame"
echo ""