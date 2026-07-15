import argparse
from pathlib import Path
from sys import stderr


from .converter import convert
from .i18n import _


def main() -> int:
    parser = argparse.ArgumentParser(
        description=_("Converts a CSV file to Excel format or vice versa")
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=Path,
        metavar=_("INPUT"),
        help=_("Input file"),
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        metavar=_("OUTPUT"),
        help=_("Output file"),
    )

    args = parser.parse_args()

    try:
        convert(args.input, args.output)
        print(_("Conversion successful"))
        return 0
    except FileNotFoundError as error:
        print(_("File not found: %s") % error.filename, file=stderr)
        return 1
    except ValueError as error:
        print(_("Error processing file: %s") % error, file=stderr)
        return 2
    except Exception as error:
        print(_("Error processing file: %s") % error, file=stderr)
        return 3
