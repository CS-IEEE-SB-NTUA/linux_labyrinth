#!/bin/python3
from os import system

system("find . | sort >> i && cat ./dir1/* >> i && cat ./dir2/* >> i")

f = open('i','r')

system('rm i')

intended = [".",
            "./dir1",
            "./dir1/file1",
            "./dir1/file2",
            "./dir2",
            "./dir2/file1",
            "./dir2/file3",
            "./HINT",
            "./validate",
            "14m th3 c0nt3nt 0f f1l3 0n3",
            "Th3 Cont3nt Of th3 th1rd f1l3 1 4m ~ Yoda"
            ]

lines = f.readlines()

dir1 = False
dir2 = False
file11 = False
file12 = False
file21 = False
file23 = False
copies1 = False
c1 = 0
copies2 = False
c2 =0
junk = False
if ("./dir1\n" in lines):
    dir1 = True
if ("./dir2\n" in lines):
    dir2 = True
if("./dir1/file1\n" in lines):
    file11 = True
if("./dir1/file2\n" in lines):
    file12 = True
if("./dir2/file1\n" in lines):
    file21 = True
if("./dir2/file3\n" in lines):
    file23 = True

c1 = lines.count("14m th3 c0nt3nt 0f f1l3 0n3\n") 

c2 = lines.count("Th3 Cont3nt Of th3 th1rd f1l3 1 4m ~ Yoda\n")

if(len(lines)>14):
    if (len(set(intended)-set(lines)) == 0):
        junk = True

if (not dir1):
    print("You have deleted dir1!!! call someone to help you")
    # exit()
if (not file11 and not file21):
    print("You have deleted file1!!! call someone to help you")
    # exit()
if (not file11 and file21):
    print("you have moved file1 instead of copying it")
if (file11 and file12 and c1<2):
    print("One copy of file1 is wrong")
if (file23 and c2<1):
    print("you have corrupted file3. Call someone to help you")
    # exit()
if (dir1 and not file12):
    print("you have to create file2 in dir1")
if ( not dir2):
    print("you have to create dir2")
if (dir2 and not file21):
    print("you have to copy file1 to dir2")
if (dir2 and not file23):
    print("you have to move file3 to dir2")
if (not junk):
    print("you have more files than intended. Try deleting some junk")
if (dir1 and dir2 and file11 and file12 and file23 and file21 and junk):
    print ("The Room is Ready! Well Done")
# else :print(dir1 , dir2 , file11 , file12 , file23 , file21 , junk)


# for line in lines:
#     print(f"-{line}-")



