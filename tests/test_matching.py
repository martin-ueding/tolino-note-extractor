from tolino_note_extractor.matching import match_notes


EXAMPLE = """

-----------------------------------

The Mythical Man-Month (Brooks, Jr. Frederick P.)
Markierung auf Seite 33-34: " For the human makers of things, the incompletenesses and inconsistencies of our ideas become clear only during implementation. Thus it is that writing, experimentation, "working out" are essential disciplines for the theoretician."
Hinzugefügt am 18.12.2025 | 8:02

-----------------------------------

Cibola Burn (Corey, James S. A.)
Markierung auf Seite 31: "“I’m sorry, sir,” Wei said. “I was out of line.”

  “Not a problem, because it’s not going to happen again,” Murtry said. "
Hinzugefügt am 29.01.2026 | 15:29

-----------------------------------
"""


def test_single() -> None:
    expected = [
        {
            "title": "The Mythical Man-Month",
            "author": "Brooks, Jr. Frederick P.",
            "type": "Markierung",
            "note": ' For the human makers of things, the incompletenesses and inconsistencies of our ideas become clear only during implementation. Thus it is that writing, experimentation, "working out" are essential disciplines for the theoretician.',
        },
        {
            "title": "Cibola Burn",
            "author": "Corey, James S. A.",
            "type": "Markierung",
            "note": """“I’m sorry, sir,” Wei said. “I was out of line.”

  “Not a problem, because it’s not going to happen again,” Murtry said. """,
        },
    ]
    assert match_notes(EXAMPLE) == expected
