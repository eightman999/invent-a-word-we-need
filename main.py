import os

TEXT = "Cozzle (v.) - to nudge an object two inches to the left while looking for it, in case that helps."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
