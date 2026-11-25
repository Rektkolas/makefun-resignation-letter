"""Make.fun entry: The Funniest One-Line Resignation Letter.

Writes one line to /output/entry.txt (ENTRY_OUTPUT override for local
testing).
"""
import os

LINE = 'Effective immediately, I resign: 43,200 runs a month, zero thanks, and the one morning I sleep in, everyone files a bug report.'


def write_line(path: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        write_line(output_path)
    except OSError:
        # The grader's /output may be unavailable locally; fall back to
        # ./output/entry.txt so the entry can still be tested by hand.
        write_line(os.path.join(os.getcwd(), "output", "entry.txt"))


if __name__ == "__main__":
    main()
