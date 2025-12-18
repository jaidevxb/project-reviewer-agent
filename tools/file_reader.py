import os

ALLOWED_EXT = (".py", ".js", ".md", ".json", ".yaml", ".yml")
MAX_SIZE = 50_000

def read_file(base_path, rel_path):
    full_path = os.path.join(base_path, rel_path)

    if not rel_path.endswith(ALLOWED_EXT):
        return None
    if not os.path.exists(full_path) or os.path.getsize(full_path) > MAX_SIZE:
        return None

    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
