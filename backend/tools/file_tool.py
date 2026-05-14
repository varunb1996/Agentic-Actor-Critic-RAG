def read_file(file_path):

    try:

        with open(file_path, "r", encoding="utf-8") as f:

            return f.read()

    except Exception as e:

        return f"File read error: {e}"