#!/bin/sh
set -e

python3 -m venv venv

. venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e .

echo "Installation complete!"
echo "Run: csv-to-excel -h"