# string to search in file
word = 'interpreted'
with open(r'C:\Users\HP\PycharmProjects\Luminar\File\demofile3.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)