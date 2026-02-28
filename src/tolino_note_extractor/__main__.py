import collections
import pprint
import argparse
import pathlib

from .matching import match_notes


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract notes from Tolino eBooks")
    parser.add_argument("notes_file", type=pathlib.Path)  # noqa: F821
    args = parser.parse_args()

    with open(args.notes_file) as f:
        content = f.read()

    sorted_notes = collections.defaultdict(list)
    for note in match_notes(content):
        if note["type"] != "Markierung":
            continue
        sorted_notes[f"{note['author']}: {note['title']}"].append(note["note"])

    for author_title, notes in sorted(sorted_notes.items()):
        print(f"# {author_title}")
        print()
        for note in notes:
            print(note)
            print()
            print("---")
            print()


if __name__ == "__main__":
    main()
