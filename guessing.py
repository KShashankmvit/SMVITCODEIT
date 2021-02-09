# program to guess a randomly generated number by computer in 5 turns
import random
num= random.randint(10,50)
turns=0
while turns<5:
    a=int(input("enter a number"))
    if a==num:
        print("very good u cracked it")
        break;
    else:
        print("wrong!")
    turns+=1
else:
    print("sorry correct answer is ",num)
    print("Better luck next time")