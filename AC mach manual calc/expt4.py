import math
import cmath
import time
start_time = time.time()

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
print(" -------********--------")
print("Pi0: {:.3f}".format(pi0))
print("PiS: {:.3f}".format(pis))
print("Iw: {:.3f}".format(iw))
print("Iu: {:.3f}".format(iu))
print("X0: {:.3f}".format(x0))
print("R0: {:.3f}".format(r0))
print("R01: {:.3f}".format(r01))
print("Z01: {:.3f}".format(z01))
print("X01: {:.3f}".format(x01))
print("R2: {:.3f}".format(r2))
print("X1: {:.3f}".format(x1))
print("I0: {:.3f}".format(i0))

while 1:
    i2o=ill=0
    s=float(input("Enter s value(1/100): "))
    ss=(2.56+(r2/s))                  #2.56 is R1
    c=complex(ss,x01)
    vph=(v1/1.7320508)
    i21=complex(vph/c)
    #pi=i21.imag
    mag1,ang1=cmath.polar(i21)
    il=(i21+i0)
    mag2,ang2=cmath.polar(il)
    rl=r2*((1/s)-1)
    Pout=(3*(math.pow(mag1,2))*rl) 
    Pin=((1.7320508)*(v1)*(mag2)*(math.cos(math.radians(math.degrees(ang2)))))
    sp=(1500*(1-s))
    trq=(Pout*60)/(2*3.141592654*sp)
    
    print("Il: {:.3f} ".format(mag2))
    print("Cos pi: {:.3f} ".format((math.cos(math.radians(math.degrees(ang2))))))
    print("Speed:  {:.3f} ".format(sp))
    print("Torque:  {:.3f} ".format(trq))
    print("Pout: {:.3f} ".format(Pout))
    print("Pinp: {:.3f} ".format(Pin))
    print("Effciency: {:.3f} ".format(((Pout/Pin)*100)))
    print("---------------------------------------------------------")
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

