import math
import cmath
#v1,i1,w1,v2,i2,w2=float(input("Enter Voc: ")),float(input("Enter Ioc: ")),float(input("Enter Woc: ")),float(input("Enter Vsc: ")),float(input("Enter Isc: ")),float(input("Enter Wsc: "))
v1=415
i1=1.9
w1=400
v2=138
i2=8.2
w2=760
pi0=math.degrees(math.acos((w1)/(1.7320508*v1*i1)))
pis=math.degrees(math.acos((w2)/(1.7320508*v2*i2)))
iw=i1*(math.cos(math.radians(pi0)))
iu=math.sqrt((i1**2)-(iw**2))
x0=(v1/1.7320508)/iu
r0=(v1/1.7320508)/iw
r01=w2/(3*(math.pow(i2,2)))
z01=(v2/1.7320508)/i2
x01=math.sqrt((z01**2)-(r01**2))
r2=(r01-2.56)            #2.56 is R1
x1=(x01/2)
i0=complex(iw,iu)

while 1:
    i2o=ill=0
    s=float(input("Enter s value(1/100): "))
    ss=(2.56+(r2/s))                  #2.56 is R1
    c=complex(ss,x01)
    vph=(v1/1.7320508)
    i21=complex(vph/c)
    il=(i21+i0)
    mag2,ang2=cmath.polar(il)
    Pin=((math.sqrt(3))*(v1)*(mag2)*(math.cos(math.radians(math.degrees(ang2)))))
    print(math.degrees(ang2))
    print(mag2)
    print("Cos pi: {:.3f} ".format((math.cos(math.radians(math.degrees(ang2))))))
    print("Pinp: {:.3f} ".format(Pin))
    print(i21)