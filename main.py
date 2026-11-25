"""Write one useless superpower line to entry.txt."""

import os
import tempfile


LINE = "I can make a pretzel's holes trade places."
CHAR_LIMIT = 140


def validate(text):
    if not text.strip():
        raise ValueError("Superpower line must not be blank.")
    if len(text) > CHAR_LIMIT:
        raise ValueError("Superpower line must be at most 140 characters.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as output:
        output.write(LINE)


if __name__ == "__main__":
    main()
