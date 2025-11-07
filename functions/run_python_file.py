import os
import subprocess
import sys


def run_python_file(working_directory, file_path, args=[]):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    command = ['python', file_path] + args
    try:
        rep = subprocess.run(args=command,
                       cwd=abs_working_directory,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       timeout=30,
                       text=True)
        if not rep.stdout or rep.stdout.strip() == "":
            return "No output produced."

        message = f'STDOUT: {rep.stdout}\n STDERR: {rep.stderr} \n '
        if rep.returncode != 0:
            message +=  f'Process exited with code {rep.returncode}'
        return message

    except Exception as e:
        return f"Error: executing Python file: {e}"

