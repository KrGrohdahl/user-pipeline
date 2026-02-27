def parse_bool(value, default=False):
    if value is None:
        return default

    v = value.strip().lower()
    if v in ("true", "t", "1", "yes", "y"):
        return True
    if v in ("false", "f", "0", "no", "n"):
        return False

    return default


def load_users_from_file(filename):
    users = []

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            clean_line = line.strip()

            # Skip blank lines
            if not clean_line:
                continue

            parts = [p.strip() for p in clean_line.split(",")]

            # Require at least name and is_active
            if len(parts) < 2:
                print(f"Skipping line {line_number}: not enough fields -> {clean_line}")
                continue

            name = parts[0]
            is_active = parse_bool(parts[1], default=False)
            is_admin = parse_bool(parts[2], default=False) if len(parts) > 2 else False

            users.append({
                "name": name,
                "is_active": is_active,
                "is_admin": is_admin
            })

    return users