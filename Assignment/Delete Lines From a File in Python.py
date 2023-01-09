# list to store file lines
lines = []
# read file
with open(r"C:\Users\HP\PycharmProjects\Luminar\File\demofile3.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"C:\Users\HP\PycharmProjects\Luminar\File\demofile3.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in [1, 2]:
            fp.write(line)