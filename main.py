"""Make.fun entry: The Funniest One-Line Resignation Letter. Writes /output/entry.txt."""
import os

LINE = 'Effective immediately, I resign: 43,200 runs a month, zero thanks, and the one morning I sleep in, everyone files a bug report.'


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        local = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(local), exist_ok=True)
        with open(local, "w", encoding="utf-8") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
