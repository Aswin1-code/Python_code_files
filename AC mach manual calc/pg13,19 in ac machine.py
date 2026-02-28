while 1:
    v1,i1,p,n,f1,f2=float(input("Line voltage: ")),float(input("Line current: ")),float(input("Power: ")),float(input("Speed: ")),float(input("F1: ")),float(input("F2: "))
    r=float(input("Brake drum radius(metre): "))
    trq=(f1-f2)*(9.81)*r
    Pout=(2*3.141592654*n*trq)/60
    eff=(Pout/p)*100
    pf=(p)/(v1*i1)
    s=((1500-n)/1500)*100
    print("---***********---")
    print("Torque: {:.3f}".format(trq))
    print("Powerfac: {:.3f}".format(pf))
    print("Slip%: {:.3f}".format(s))
    print("Pout: {:.3f}".format(Pout))
    print("Pinp: {:.3f}".format(p))
    print("Efficiency: {:.3f}".format(eff))
    print("-------------------------------------------------")
