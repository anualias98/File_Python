import os.path

# file to check
file_path = r'C:\Users\HP\PycharmProjects\Luminar\File\demofile3.txt'

flag = os.path.isfile(file_path)
if flag:
    print(f'The file {file_path} exists')
else:
    print(f'The file {file_path} does not exist')
    # you can create it if required
