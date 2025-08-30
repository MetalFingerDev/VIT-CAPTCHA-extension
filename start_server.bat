@echo off
ECHO Checking for virtual environment...

REM Check if the venv directory exists. If not, create it.
if not exist venv (
    ECHO Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
ECHO Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies from requirements.txt
ECHO Installing dependencies...
pip install -r requirements.txt

REM Run the Python application
ECHO Starting Flask server...
python app.py