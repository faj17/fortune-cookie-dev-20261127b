"""One line of fortune-cookie wisdom for a software developer.

The whole entry is a single sentence about the oldest developer truth
there is: a green test suite is not proof the code is right, only proof
the bug has not been caught yet. The script validates the line against
the bounty gate (one sentence, 1-120 characters, ends with a full stop)
and writes it — with no trailing newline — to /output/entry.txt.
"""

from pathlib import Path

# The fortune itself: one sentence, exactly 99 characters.
# A passing test is no alibi for the code — it only means the bug
# found a corner the tests never look into.
FORTUNE = (
    "A passing test proves nothing except that the bug has learned "
    "to hide where your tests do not look."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 120


def validate(line: str) -> str:
    """Strip and sanity-check the fortune; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"fortune must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("fortune must not contain control characters")
    if not text.endswith("."):
        raise ValueError("fortune must end with a full stop")
    if ". " in text:
        raise ValueError("fortune must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(FORTUNE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
