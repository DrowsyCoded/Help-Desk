@echo off
cd /d "%~dp0"
echo Checking Python and dependencies...
python --version
if errorlevel 1 (
    echo.
    echo ERROR: 'python' was not found. Is Python installed and on PATH?
    pause
    exit /b 1
)

python -m pip show flask >nul 2>&1
if errorlevel 1 (
    echo Flask is not installed for this Python -- installing it now...
    python -m pip install flask
)

echo.
echo Starting the Help Desk Tracker...
echo.
python app.py

echo.
echo The app stopped or failed to start - see any error message above.
pause
