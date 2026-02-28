from ast import Continue

print("Hi !\n Lets have some conversation")
a=str(input("How are you ?"))
b="fine"
c="i am fine what about you"
if str(a)==str(b) :
    print("\tokay")
elif str(a)==str(c):
    print("\tMe too fine")
else:
    Continue
    
e=str(input("Did you had your lunch ?"))
f="yes"
if str(e)==str(f):
    print("\tjust now i had finished my lunch")
else:
    Continue

g=str(input("When will you go to sleep ?"))
if int(g)>=int(11):
  print("\tgo to bed early")
elif int(g)>=int(10):
    print("\tGo to bed now")
    print("\n\tgood night")
else:
    print("Go and read")
      