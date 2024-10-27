import os
print(os.name)
print(os.getcwd())

print(os.listdir(os.curdir))
# print(os.environ)


import pathlib
cur_path = pathlib.Path()
print(cur_path)
print(cur_path.cwd())
