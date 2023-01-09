import os

# folder path
dir_path = r'C:\Users\HP\PycharmProjects\Luminar\function'

# list to store files
res = []
# Iterate directory
for file in os.listdir(dir_path):
    # check only text files
    if file.endswith('.txt'):
        res.append(file)
print(res)