file = open("test.txt")

#print(file.read())          # To read all the content of the file and to print the same using "print command"

#file.seek(0)                # Reset the pointer to the beginning of the file

#print(file.read(22))        # Read n number of characters using the parameter

#file.seek(0)

#print(file.readline())      # To read one single line
#print(file.readline())
#print(file.readline())

#fileRead = (file.readline())
#
# while fileRead != "":
#     print(fileRead)
#     fileRead = file.readline()

for line in file.readlines():           # This is the method in which values gets stored in the list using readlines()
    print(line)

file.close()


