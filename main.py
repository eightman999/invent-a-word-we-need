import os

TEXT = "Replapse (n.) - the relapse of replying to a text thread you had successfully escaped."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
