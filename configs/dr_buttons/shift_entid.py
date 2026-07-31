import os

OFFSET = 8

def offset_ini_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        stripped = line.strip()

        # Keep comments and empty lines unchanged
        if not stripped or stripped.startswith(";"):
            new_lines.append(line)
            continue

        parts = line.split()

        # Modify only lines where the first item is an integer
        try:
            parts[0] = str(int(parts[0]) + OFFSET)
            new_lines.append(" ".join(parts) + "\n")
        except (ValueError, IndexError):
            new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Updated: {filepath}")


def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(folder):
        if filename.lower().endswith(".ini"):
            filepath = os.path.join(folder, filename)
            offset_ini_file(filepath)


if __name__ == "__main__":
    main()