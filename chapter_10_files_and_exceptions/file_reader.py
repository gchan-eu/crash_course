file_path = 'C:\\Users\\gchan\\code\\python\\crash_course\\chapter_10_files_and_exceptions\\'
file_name = 'pi_digits.txt'

with open(file_path + file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

