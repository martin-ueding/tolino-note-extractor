import pprint
import re

PATTERN = re.compile(
    r'(?P<title>.+) \((?P<author>.+)\)\n(Lesezeichen|Markierung) auf Seite (?P<page>\d+): "(?P<note>.+)"\nHinzugefügt am \d+\.\d+\.d+ \| \d+:\d+',
    re.DOTALL,
)


def match_notes(notes: str):
    matches = re.findall(PATTERN, notes)
    pprint.pprint(matches, compact=True)
