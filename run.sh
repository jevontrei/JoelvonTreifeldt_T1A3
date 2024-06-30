# see the lessons discord server week 8

# !/bin/bash
python3 -m venv virtualenv

# Activate virtualenv
source virtualenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
python3 src/main.py

# Deactivate virtualenv
deactivate