from pathlib import Path

file_path = 'C:\\Users\\gchan\\code\\python\\crash_course\\chapter_10_files_and_exceptions\\'
file_name = 'learning_python.txt'

#with open(file_path + file_name) as file_obj:
#    contents = file_obj.read()

#with open(file_path + file_name) as file_obj:
#    line = file_obj.readline()
#    print(line)

path = Path(file_path + file_name)
contents = path.read_text()
print(contents)

