#Write a Python program to build a secure password generator.

import random

lower='abcdefghijklmnopqrstuv'
upper=lower.upper()
special='~!@#$%^&*()_+-=\}]{[|;:,<.>?/'
number='0123456789'

all=lower+upper+number+special

length=int(input("Enter the length of your password: "))

password=""

if (length >=8) and (length <=15):
    c=1

    for i in range(length-2):

        if i==4:
            password+=random.choice(special)
        if i==1:
            password+=random.choice(number)
        else:
            password+=random.choice(all)

else:
    c=0

    if length<=4:
        print("Password is too short")
    else:
        print ("Password must be between 8 to 15 characters long")

if c==1:
    print('Password is :',password)
else:
    print('Password is not generated please try again !!!')

'''
1) Enter the length of your password: 7
Password must be between 8 to 15 characters long
Password is not generated please try again !!!

2) Enter the length of your password: 4
Password is too short
Password is not generated please try again !!!

3) Enter the length of your password: 10
Password is : U1j/[gQkS

4) Enter the length of your password: 15
Password is : K4_#<fh!_gE-6>

5) Enter the length of your password: 16
Password must be between 8 to 15 characters long
Password is not generated please try again !!!

'''
