from pathlib import Path
import pandas


def convert(input_file: Path, output_file: Path) -> None:
    """
    Converts a CSV file to Excel or vice versa
    """
    if str(input_file).endswith(".csv"):
        data = pandas.read_csv(input_file)
        data.to_excel(output_file, index=False)
    else:
        data = pandas.read_excel(input_file)
        data.to_csv(output_file, index=False)
