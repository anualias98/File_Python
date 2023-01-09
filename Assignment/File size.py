import os.path

# file to check
file_path = r'C:\Users\HP\PycharmProjects\Luminar\File\demofile3.txt'

sz = os.path.getsize(file_path)
print(f'The {file_path} size is', sz, 'bytes')
