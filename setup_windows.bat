@echo off
setlocal

python -m venv venv

call venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install -e .

echo Installation complete!
echo Run: csv-to-excel -h

pause