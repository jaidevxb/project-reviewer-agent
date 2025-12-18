import os
import tempfile
from git import Repo

IGNORE_DIRS = {".git", "node_modules", "__pycache__", "venv"}

def load_repo(repo_url: str):
    temp_dir = tempfile.mkdtemp()
    Repo.clone_from(repo_url, temp_dir)

    file_tree = []
    for root, dirs, files in os.walk(temp_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, temp_dir)
            file_tree.append(rel_path)

    return temp_dir, file_tree
