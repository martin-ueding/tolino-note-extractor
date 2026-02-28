import re

# Match the separator, then the title/author, then the page info, and finally the timestamp.
# Handles non-breaking spaces (\xa0) and normal spaces.
PATTERN = re.compile(
    r'-{10,}\s*\n\s*(?P<title>.+?)\s+\((?P<author>.+?)\)\n(?:Lesezeichen|Markierung)[\s\xa0]auf[\s\xa0]Seite[\s\xa0](?P<page>[\d-]+): "(?P<note>.+?)"\nHinzugefügt[\s\xa0]am[\s\xa0](?P<date>\d{2}\.\d{2}\.\d{4}) \| (?P<time>\d{1,2}:\d{2})',
    re.DOTALL,
)


def match_notes(notes: str):
    matches = [m.groupdict() for m in re.finditer(PATTERN, notes)]
    return [
        {
            "title": m["title"].strip(),
            "author": m["author"].strip(),
            "note": m["note"],
        }
        for m in matches
    ]
