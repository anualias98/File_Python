with open(r"C:\Users\HP\PycharmProjects\Luminar\File\demofile3.txt", 'r') as fp:
    # lines to read
    line_numbers = [1, 2]
    # To store lines
    lines = []
    for i, line in enumerate(fp):
        # read line 4 and 7
        if i in line_numbers:
            lines.append(line.strip())
        # elif i > 7:
        #     # don't read after line 7 to save time
        #     break
print(lines)
