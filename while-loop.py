# A while loop repeatedly executes a block of code as long as a specified condition remains True

it = 4

while it>1:
    print(it)
    it = it - 1

print("While loop execution is done")

# In the above scenario if you want 3 to not print with 4 and 2

iit = 4

while iit>1:
    if iit != 3:
        print(iit)
    iit = iit - 1

print("while loop execution is done")

# Is there are many numbers and I want to know if 3 is present in that number
# When it gets 3 then the while loop will get stops and not execute further

ti = 20

while ti>1:
    if ti == 9:
        ti = ti - 1
        continue            # this skips the below code. That is why we wrote "ti = ti - 1" again to execute.
    if ti == 3:
        break
    print(ti)
    ti = ti - 1
print("This while loop is done")
