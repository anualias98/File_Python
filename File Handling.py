# f = open("demofile2.txt", "r")
# print(f.read())
# f = open("demofile3.txt", "r")
# # f.write("Hello World!Now the file has more content!")
# # f.close()
# print(f.read())
#create
# f = open("myfile.txt", "x")
# f = open("demofile3.txt", "r")
# print(f.readline())
#remove

# import os
# if os.path.exists("demofile2.txt"):
#   os.remove("demofile2.txt")
# else:
#   print("The file does not exist")
"""1.Read a file line by line and store it into a list"""
# file=open("demofile3.txt")
# lines=file.read()
# print(file.read())
# list=lines.split('\n')
# print(list)
"""2.Program to find largest word in that file"""
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word('demofile3.txt'))
