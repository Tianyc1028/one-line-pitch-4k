"""One-line pitch entry for "A Day of One-Line Pitches" (make.fun).

Writes a single persuasive sentence to /output/entry.txt: it invites a
friend who has never coded to describe their app idea in plain words and
let an AI agent on make.fun build a working first version of it.

Python 3.13, standard library only, no network. Deterministic: the same
bytes are written on every run.
"""

import os
import re

PITCH = (
    "Just describe the app idea you've been carrying around in plain words, "
    "and an AI agent on make.fun will build a working first version you can "
    "try and tweak, no coding needed, so it finally stops living only in "
    "your head."
)

MAX_CHARS = 240


def is_one_sentence(text: str) -> bool:
    """One sentence: non-empty, ends with a period, and contains no
    sentence boundary (a period followed by a space and a capital letter).
    The period inside "make.fun" is followed by a lowercase letter, so it
    is not a sentence boundary."""
    stripped = text.strip()
    if not stripped or not stripped.endswith("."):
        return False
    return re.search(r"\.\s+[A-Z]", stripped) is None


def main() -> None:
    assert is_one_sentence(PITCH), "pitch must be exactly one sentence"
    assert 1 <= len(PITCH) <= MAX_CHARS, (
        f"pitch must be 1-{MAX_CHARS} characters, got {len(PITCH)}"
    )
    assert PITCH.strip() == PITCH, "pitch must not have surrounding whitespace"

    output_dir = "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(PITCH)
    except OSError:
        # Local fallback only: the grader provides a writable /output.
        here = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(here, "output")
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(PITCH)

    print(f"Wrote {len(PITCH)} characters to {path}")


if __name__ == "__main__":
    main()
