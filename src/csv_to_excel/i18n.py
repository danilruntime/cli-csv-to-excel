from pathlib import Path
import gettext
import locale
import argparse

LOCALE_DIR = Path(__file__).parent / "locale"
raw_lang = locale.getlocale()[0] or "en"
user_lang = raw_lang[:2].lower()
translation = gettext.translation(
    "messages",
    localedir=LOCALE_DIR,
    languages=[user_lang],
    fallback=True,
)

_ = translation.gettext

# Give argparser translation flag
setattr(argparse, "_", _)
