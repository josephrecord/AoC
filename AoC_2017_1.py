from itertools import *

def rotate(l, n):
    return l[n:] + l[:n]

with open("C:\\Users\\jrecord\\Documents\\AoC_2017_1.txt") as f:
    l = f.readline()

n = int(l)
num = [int(d) for d in str(n)]
length = len(num)

num_rot1 = rotate(num,1)
num_rot2 = rotate(num,length//2)

sum1 = 0
sum2 = 0

for i in range(length):
    if num[i] == num_rot1[i]:
        sum1 = sum1 + num[i]

for i in range(length):
    if num[i] == num_rot2[i]:
        sum2 = sum2 + num[i]


print(sum1)
print(sum2)
