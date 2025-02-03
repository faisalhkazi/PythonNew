# Below is the moto of this practice file
# First we will read the file
# Then we will reverse the file
# In the end we will write the reverse content in the file

with open("test.txt", "r") as reader:       #This is to read the text file in read mode "r". In this, no need to close the file.
    content = reader.readlines()            # This is to store the content in variable
    reversed(content)                       # This is to reverse the content
    with open("test.txt", "w") as writer:   # This will again open the file in the write mode "w"
        for contentr in reversed(content):  # This will create a loop in which it will write the content line by line.
            writer.write(contentr)
