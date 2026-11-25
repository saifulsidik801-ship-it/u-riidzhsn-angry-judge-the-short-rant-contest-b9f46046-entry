# Angry Judge — one short rant about a small everyday annoyance, max 400 chars.
# Writes the entry text to /output/entry.txt; judge scores the rant alone.
"""Angry Judge entry: one short rant about a small everyday annoyance.

Writes the rant to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Gate: UTF-8 text of 1-400 characters, not only whitespace.
"""
import os

RANT = (
    "My Wi-Fi only dies during the one call that matters. Four bars all morning, "
    "then the second my boss says 'great work, tell us more' \u2014 frozen face, "
    "robot voice, reconnecting. It came back the instant the meeting ended, like "
    "it was waiting outside the door, smug. I pay for gigabit and get ghosted by "
    "a router that has never once, in its entire life, been wrong about when to quit."
)

def main():
    if not 1 <= len(RANT) <= 400 or not RANT.strip():
        raise ValueError(f"rant must be 1-400 non-blank chars, got {len(RANT)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(RANT)
    print(f"wrote {len(RANT)} chars to {os.path.join(out_dir, 'entry.txt')}")

if __name__ == "__main__":
    main()
