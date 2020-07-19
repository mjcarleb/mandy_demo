# with open('what_are_context_managers.txt', 'w') as infile:
#     infile.write('Something')
# print(infile.closed)

from contextlib import contextmanager
@contextmanager
def OpenFile(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with OpenFile('mandyfile.txt', 'w') as f:
    f.write('Writing to my file')
print(f)
print(f.closed)

#Context manager for working with files
class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for _ in range(6):
    with File('myfile.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)
print(files)
print(len(files))

# class OpenFile:
#     def __init__(self, file, mode):
#         self.file = file
#         self.mode = mode
#
#     def __enter__(self):
#         self.f = open(self.file, self.mode)
#         return self.f
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.f.close()
#
# with OpenFile('file.txt', 'w') as f:
#     f.write('Something to write to mine')
# print(f.closed)