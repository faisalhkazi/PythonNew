obj = [5, 9, 6, 7, 5, 44, 89, 67, 41, 34]

for i in obj:
    print(i)
    print(i*2)
    print(" ")

# Sum of first Natural numbers 1+2+3+4+5 = 15
summation = 0
for j in range(1,6):  # It will take the range(i,j) of (i,j-1). THis is similar in Java for(i=0,i<5,i++)
    summation = summation + j
    print(j)

print(summation)


