
#getting letter as input
letter=''
while not letter.isalpha():
    letter=input("Enter any alphabet")
print("you have entered ",letter)     

#number guess game
'''
import random
num = random.randint(1,20)
guess=int(input("Can you guess a number I'm thinking ,it between (0-20)"))
while num!=guess:
    if num>guess:
        print("you guessed smaller number")
        guess=int(input("Try again :"))
    else:
        print("you guessed larger number")
        guess=int(input("Try again :"))
print("you entered a correct number ."+"My Number "+str(num)+"="+" Your Guess "+str(guess))

'''
#print upto n
'''
n=''
while not n.isnumeric():
     n=input("Enter a number")
num=1
while num<=int(n):
     print(num)
     num+=1
'''
    