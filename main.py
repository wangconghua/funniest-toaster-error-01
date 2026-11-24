#!/usr/bin/env python3
"""The Funniest Toaster Error Message: the error a kitchen toaster shows
its owner when something goes wrong."""

import os

MESSAGE = "ERROR: Bread jammed. Do not use a fork. We have seen what you do with forks."

OUT_PATH = "/output/entry.txt"

# Words that explain the joke instead of being the joke. A funny line must
# land on its own; if it has to say it is funny, it is not.
META_HUMOR_WORDS = ("funny", "joke", "haha", "lol", "hilarious")

# How a real appliance opens an error message.
ERROR_PREFIXES = ("ERROR", "WARNING", "E-")


def validate(message: str) -> None:
    if not (1 <= len(message) <= 120) or message.isspace() or "\n" in message:
        raise ValueError("entry must be one line of 1-120 characters, not only whitespace")
    if message != message.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in message:
        raise ValueError("entry must not contain double spaces")
    if not message.startswith(ERROR_PREFIXES):
        raise ValueError("entry must read like a real appliance error message")
    lowered = message.lower()
    for word in META_HUMOR_WORDS:
        if word in lowered:
            raise ValueError(f"entry must not explain its own joke (found {word!r})")


def main():
    # The gate wants 1-120 characters, not only whitespace, on a single line.
    # The joke: a toaster that has watched its owner fish jammed bread out
    # with a fork one time too many, and now refuses to pretend otherwise.
    # "Bread jammed" is literal and a pun at once; the fork warning is the
    # real safety rule every toaster prints; the last clause turns it into
    # an accusation from an appliance that has been keeping score.
    validate(MESSAGE)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
