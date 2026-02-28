#Emf
import math

v=239.6
i=4
r=2.4
x=29.903

while 1:
    cospi=float(input("Enter cospi: "))
    sinpi=float(input("Enter sinpi: "))
    a1=math.pow(((v*cospi)+(i*r)),2)
    a2=math.pow(((v*sinpi)+(i*x)),2)
    a3=math.sqrt(a1+a2)
    reg1=((a3-v)/v)*100
    b1=math.pow(((v*cospi)+(i*r)),2)
    b2=math.pow(((v*sinpi)-(i*x)),2)
    b3=math.sqrt(b1+b2)
    reg2=((b3-v)/v)*100
    print("Lag:{:.2f}".format(a3))
    print("Lead:{:.2f}".format(b3))
    print("Lag reg% :{:.2f}".format(reg1))
    print("Lead reg% :{:.2f}".format(reg2))
    print("-------------------------------------")

#mmf
while 1:
    sinpi=float(input("Enter sinpi value: "))
    print("Ilag: {:.2f}".format(math.sqrt(1.6164+(1.008*(sinpi)))))
    e1=float(input("Enter E0: "))
    print("Reg%: {:.2f}".format(((e1-v)/v)*100))
    print("-----")
    print("Ilead: {:.2f}".format(math.sqrt(1.6164-(1.008*(sinpi)))))
    e2=float(input("Enter E0: "))
    print("Reg%: {:.2f}".format(((e2-v)/v)*100))
    print("---------------------------------------")

#zpf
while 1:
    cospi,sinpi=float(input("Enter cospi: ")),float(input("Enter sinpi: "))
    print("-----------\nLagging pf -----------")
    print("E={:.2f}".format(math.sqrt((pow(((239.6*cospi)+(9.6)),2))+(pow(((239.6*sinpi)+(15)),2)))))
    i1=float(input("Enter If1= "))
    print("If= {:.3f}".format(math.sqrt((i1**2)+(0.39**2)+(0.78*i1*sinpi))))
    E0=float(input("Enter Eo: "))
    print("R%={:.3f}".format(((E0-239.6)/239.6)*100))
    
    print("---------------------\nleading pf--------")
    print("E={:.2f}".format(math.sqrt((pow(((239.6*cospi)+(9.6)),2))+(pow(((239.6*sinpi)-(15)),2)))))
    i1=float(input("Enter If1= "))
    print("If= {:.3f}".format(math.sqrt(((i1**2)+(0.39**2))-(0.78*i1*sinpi))))
    E0=float(input("Enter Eo: "))
    print("R%={:.3f}".format(((E0-239.6)/239.6)*100))
    print("------------------------------------------------------------------------------------------------------")

    