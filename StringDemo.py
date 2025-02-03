str = "all.in.one.place.online"

str1 = "Is the one place solution"

str3 = "allinoneplace"

print(str[1])

print(str1[0:2])    # Is you want sub-string in Python

print(str + " " + str1)    # Concatenation

print(str3 in str)      # To validate if the given name is present

var = str.split(".")

print(var)

print(var[4])

str4 = "I am great "

var2 = str4.strip()     # To remove the blank space from start and end of the word, sentence or line

print(var2)

str5 = " Removing left space "

str6 = " Removing right space "

var3 = str5.lstrip()        #To remove the blank space from left side

var4 = str6.rstrip()        # To remove the blank space from Right side

print(var3)
print(var4)


