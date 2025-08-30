#!/bin/bash

echo "Checking for virtual environment..."

# Check if the venv directory exists. If not, create it.
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the Python application
echo "Starting Flask server..."
python3 app.py