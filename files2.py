#  files read as bytes or as chars
#  windows end of line \n\a (others- \n only)
# # decode from unicode => curent coding
# context manager

# Mode	Description
# 'r'	This is the default mode. It Opens file for reading.
# 'w'	This Mode Opens file for writing.
# If file does not exist, it creates a new file.
# If file exists it truncates the file.
# 'x'	Creates a new file. If file already exists, the operation fails.
# 'a'	Open file in append mode.
# If file does not exist, it creates a new file.
# 't'	This is the default mode. It opens in text mode.
# 'b'	This opens in binary mode.
# '+'	This will open a file for reading and writing (updating)

## write to file
f = open("file.txt", "wt")
f.write("String1\n")
f.flush()
f = open("file.txt", "at")
f.write("String added 1\n")
f.write("String added 2\n")
f.write("String added 3\n")
f.close()

## reaad from file
f = open("file.txt", "rt")
s = f.read()
print(s, end='\n')
f.close()

f = open("file.txt", "r+t", errors='ignore')  # read and write
print(f.tell())
f.seek(43)
print(f.tell())
f.write("a")
print(f.tell())
print(f.read())
f.close()


## context manager

with open("file.txt", "rt") as f:
    for line in f:
        print(line)

