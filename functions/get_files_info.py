import os

def get_files_info(working_directory, directory="."):
    child_path = os.path.join(working_directory, directory)
    abs_child = os.path.abspath(child_path)
    abs_parent = os.path.abspath(working_directory)
    if not os.path.isdir(abs_child):
        return f'Error: "{directory}" is not a directory'
    if not abs_child.startswith(abs_parent):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    messages = []
    items = os.listdir(child_path)
    for item in items:
        full_path = os.path.join(child_path, item)
        size = os.path.getsize(full_path)
        if os.path.isfile(full_path):
            message_file = f'- {item}: file_size={size} bytes, is_dir=False'
            messages.append(message_file)
        elif os.path.isdir(full_path):
            if item=="__pycache__":
                continue
            message_dir = f'- {item}: file_size={size} bytes, is_dir=True'
            messages.append(message_dir)

    return "\n".join(messages)






