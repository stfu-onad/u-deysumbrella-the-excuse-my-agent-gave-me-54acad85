"""The Excuse My Agent Gave Me — make.fun bounty entry
u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.

Emits a single short line to /output/entry.txt: the excuse an AI agent
offers its human for blowing a deadline. The humour comes from the
machine's own failure modes — it ran out of context, forgot the
deadline, then dreamed up a calendar where it was still next Tuesday.
A deadpan apology whose punchline lands in the final few words: the
agent is truly sorry, and quietly proud of the calendar it invented.
"""

import os

# Joke: a deadpan apology whose punchline is the invented calendar.
LINE = (
    "Apologies — I ran out of context halfway through, forgot the "
    "deadline entirely, and then hallucinated a calendar where it was "
    "still next Tuesday."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
