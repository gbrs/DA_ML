import os
dir_count = file_count = 0
for dir_path, dir_names, file_names in os.walk(f"./{input()}"):
    dir_count += len(dir_names)
    file_count += len(file_names)

print(file_count, dir_count)
