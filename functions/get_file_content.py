import os
from .config import MAX_CHARS

def get_file_content(working_directory, file_path):
    child_path = os.path.join(working_directory, file_path)
    abs_child = os.path.abspath(child_path)
    abs_parent = os.path.abspath(working_directory)
    if not abs_child.startswith(abs_parent):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'

    if not os.path.isfile(abs_child):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with (open(abs_child, "r") as f):
            file_content = f.read(MAX_CHARS)
            if os.path.getsize(abs_child) > MAX_CHARS:
                file_content+=f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


