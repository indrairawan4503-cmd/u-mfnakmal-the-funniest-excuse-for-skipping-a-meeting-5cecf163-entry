#!/usr/bin/env python3
"""Write the entry text to /output/entry.txt (deterministic)."""
import os

ENTRY = "I can't make the meeting, so I've sent this email instead of me — it read the agenda, makes every point I'd make, takes no questions, and unlike me it will never ask if everyone can see my screen."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass

if __name__ == "__main__":
    main()
