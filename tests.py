# import unittest
# from functions.get_files_info import get_files_info

# class TestFunctions(unittest.TestCase):
#     def test_get_current(self):
#         result = get_files_info("calculator", ".")
#         print(result)
#         self.assertEqual(result, "- main.py: file_size=729 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True")
#
#     def test_get_subdir(self):
#         result = get_files_info("calculator", "pkg")
#         print(result)
#         self.assertEqual(result, "- calculator.py: file_size=1737 bytes, is_dir=False\n- render.py: file_size=388 bytes, is_dir=False")
#
#     def test_get_bin(self):
#         result = get_files_info("calculator", "/bin")
#         print(result)
#         self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')
#
#     def test_get_outside(self):
#         result = get_files_info("calculator", "../")
#         print(result)
#         self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')
# def test():
#     result = get_files_info("calculator", ".")
#     print("Result for current directory:")
#     print(result)
#     print("")
#
#     result = get_files_info("calculator", "pkg")
#     print("Result for 'pkg' directory:")
#     print(result)
#
#     result = get_files_info("calculator", "/bin")
#     print("Result for '/bin' directory:")
#     print(result)
#
#     result = get_files_info("calculator", "../")
#     print("Result for '../' directory:")
#     print(result)

# from functions.get_file_content import get_file_content
# def test():
#     result = get_file_content("calculator", "main.py")
#     print(result)
#
#     result = get_file_content("calculator", "pkg/calculator.py")
#     print(result)
#
#     result = get_file_content("calculator", "/bin/cat")
#     print(result)

# from functions.write_file import write_file
# def test():
#     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#     print(result)
#
#     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     print(result)
#
#     result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#     print(result)
from functions.run_python_file import run_python_file
def test():
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print(result)


if __name__ == "__main__":
    test()
    # unittest.main()