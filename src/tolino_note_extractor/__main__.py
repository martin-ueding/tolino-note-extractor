import pprint
import argparse
import pathlib

from .matching import match_notes


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract notes from Tolino eBooks")
    parser.add_argument("notes_file", type=pathlib.Path)  # noqa: F821
    args = parser.parse_args()

    with open(args.notes_file) as f:
        notes = f.read()

    pprint.pprint(match_notes(notes))


if __name__ == "__main__":
    main()
