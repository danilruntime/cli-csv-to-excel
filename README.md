# Command-Line Tool to Convert CSV Files to Excel and Vice Versa
## Description
A small Python project with a solid structure and localization
## Localization
Russian/Русский
## Usage
![preview](https://raw.githubusercontent.com/danilruntime/cli-csv-to-excel/main/preview.png)
- The project is published on PyPI. You can install it using ```pip install cli-csv-to-excel```<br>
- The project can be installed as a **.whl** file from the releases ```pip install FILE.whl```<br>
- For quick setup **python venv** and start project, you can run one of the two **setup** files for **Linux** (**setup_linux.sh**) or **Windows** (**setup_windows.bat**)
- Localization files are stored as **.po** files in the **src/csv_to_excel/locale/LANG** folder and compiled using **build_messages.py**
- To edit localizations using **build_messages.py**, you need to install **polib** in your **venv**: ```pip install polib```
- To build the project, you need the **build** module. You can install it using ```pip install build``` and build the project with ```python -m build``` using **pyproject.toml**
## License
MIT License