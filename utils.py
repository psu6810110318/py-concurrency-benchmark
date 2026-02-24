def count_chars_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:

        with open(filename, "r", encoding="utf-16") as f:
            text = f.read()

    text = "".join(text.split())
    return len(text)