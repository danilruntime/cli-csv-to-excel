from typing import List
import polib


def merge_po_files(input_files: List[str], output_file: str) -> None:
    """
    Combines multiple .po files into a single .mo file
    """
    if not input_files:
        print("File list is empty")
        return

    base_po = polib.pofile(input_files[0])

    for file_path in input_files[1:]:
        current_po = polib.pofile(file_path)

        for entry in current_po:
            existing_entry = base_po.find(entry.msgid)

            if not existing_entry:
                base_po.append(entry)
            else:
                if not existing_entry.msgstr and entry.msgstr:
                    existing_entry.msgstr = entry.msgstr

    base_po.save_as_mofile(output_file)
    print(f"Successfully merged {len(input_files)} files into -> {output_file}")


def main():
    # RU
    files_to_merge = ["locale/ru/messages_argparse.po", "locale/ru/messages_custom.po"]
    merge_po_files(files_to_merge, "locale/ru/LC_MESSAGES/messages.mo")


if __name__ == "__main__":
    main()
