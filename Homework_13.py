#Task 1
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#Task 2
for x in numbers:
    if x == 254:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)


#Task3
lis = list()
while True:
    val = input("Print STOP to stop) ")
    if val != "STOP":
        lis.append(val)
    else:
        break
print(lis)


#Task4 Not completed

import os
import platform

str = "This script has the following PID: <ACTUAL_PID_HERE>." \
      " It was ran by <ACTUAL_USERNAME_HERE> to work happily on <ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>"

chars = "<"
opsys = os.name
rel = platform.release()
usr = os.getlogin()
pid = os.getppid()
print("It was ran by " + usr + f" This script has the following PID {pid}")
print(str.split(' ')[], opsys, "-", rel)

#Task5

array = [1, 2, 3, 4, 5, 6, 7, 'str', 9, 'hi']
result = []
exc = list()

for x in range(0, 3):
    largeNum = 0
    for y in range(len(array)):
        if (isinstance(array[y], int) and array[y] > largeNum):
            largeNum = array[y]
    array.remove(largeNum)
    result.append(largeNum)

for i in array:
    if (isinstance(i, int)) != True:
        exc.append(i)

print("Top 3 integers in array",result)
print("Can't parse these values", exc)


#Task6

string = input("Print your text")


all_freq = {}

def char_freq (test_str):
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1


char_freq(string)
print ("Count of all characters in string is :\n "
                                        +  str(all_freq))
                                        
                                        
                                        
#Task7

def printSpiralMatrix(N):
    for i in range(N):
        for j in range(N):


            x = min(min(i, j), min(N - 1 - i, N - 1 - j))


            if i <= j:
                print(abs((N - 2 * x) * (N - 2 * x) - (i - x) - (j - x) - (N ** 2 + 1)), end='')

            else:
                print(abs((N - 2 * x - 2) * (N - 2 * x - 2) + (i - x) + (j - x) - (N ** 2 + 1)), end='')

            print('\t', end='')
        print()


printSpiralMatrix(5)
