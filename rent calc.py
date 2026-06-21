#rent calc
import math
print("What do you want to rent ?")
print("1 = home")
print("2 = viechle or object")
print("3 = commercial property")
print("4 = error")
rent= int(input("Enter the thing name which you want to rent : "))

def v ():
    pv= int(input("Enter the purchase value of your object : "))
    erv= int (input("Enter thr expected rate value if you resale your product : "))
    ul= int (input(" Enter the useful life of obbject : "))
    print("1 = best")
    print("2 = good")
    print("3 = worse")
    m= int(input("Enter the maintainance of your object : "))
    p= int( input("Enter the profit you want in ruppees : "))
    if m == 1:
       a=(((pv-erv)/ul)+p)-((((pv-erv)/ul)+p)/10)
       return a
    elif m==2: 
        b =(((pv-erv)/ul)+p)-((((pv-erv)/ul)+p)/15)
        return b
    elif m==3:
        c=(((pv-erv)/ul)+p)-((((pv-erv)/ul)+p)/70)
        return c
    else:
        return "error"
    
def h ():
    pov= int(input("Enter the property value of your house : "))
    by= float(input("Enter the base yield of your property ( note that : base yield  in india is generally bettwen 0.02 to 0.05) : "))
    print(" Enter locality, condition and amenities in 1,2,3 only : ")
    print("1 = best")
    print("2 = good")
    print("3 = worse")
    l= int(input("Enter the locality standard of your property : "))
    cf = int(input("Enter the condition of your property : "))
    af= int(input("Enter the amenities of your property : "))
    
    if l == 1:
       aa=(pov*by)/12
    elif l==2:
        bb = ((pov*by)/12)- (((pov*by)/12)/10)
    elif l==3:
        cc=((pov*by)/12)-(((pov*by)/12)/20)
    else:
        return "error"
    
    if cf== 1:
        if l == 1:
            aaa=(pov*by)/12
        elif l==2:
            aab = bb
        elif l==3:
            aac=cc
        else:
            return "error"
       
    elif cf==2:
        if l == 1:
            bba= bb-(((pov*by)/12)/10)
        elif l==2:
            bbb=bb -(((pov*by)/12)/20)
        elif l==3:
            bbc=cc-(cc/10)
        else:
            return "error" 
    elif cf==3:
        if l== 1:
            cca=cc 
        elif l==2:
            ccb = cc- (((pov*by)/12)/10)
        elif l==3:
            ccc=cc-(((pov*by)/12)/20)
        else:
             return "error"
    else:
        return "error"
    
    
    if af == 1:
        if l== 1 and cf== 1:
            aaaa= aaa
            return aaaa 
        elif l==1 and cf==2 :
            aaab = bba
            return aaab
        elif l==1 and cf == 3:
            aaac=cca
            return aaac
        elif l==2 and cf==1:
           aaba=bba
           return aaba
        elif l== 2 and cf==2:
            aabb=bbb
            return aabb
        elif l==2 and cf==3:
            aabc=ccb
            return aabc
        elif l==3 and cf==1:
            aaca=cc
            return aaca
        elif l==3 and cf == 2:
            aacb=bbc
            return aacb
        elif l==3 and cf== 3:
            aacc=ccc
            return aacc
        else:
            return "error"
        
    elif af == 2:
        if l== 1 and cf== 1:
            bbaa= aaa -(aaa/10)
            return bbaa
        elif l==1 and cf==2 :
            bbab = bba -(bba/10)
            return bbab
        elif l==1 and cf == 3:
            bbac=cca-(cca/10)
            return bbac
        elif l==2 and cf==1:
           bbba=bba-(bba/20)
           return bbba
        elif l== 2 and cf==2:
            bbbb=bbb-(bbb/20)
            return bbbb
        elif l==2 and cf==3:
            bbbc= ccb -(ccb/20)
            return bbbc
        elif l==3 and cf==1:
            bbca=cc-(cc/30)
            return bbca
        elif l==3 and cf == 2:
            bbcb=bbc-(bbc/30)
            return aacb
        elif l==3 and cf == 3:
            bbcc=ccc -(ccc/30)
            return bbcc
        else:
            return "error"
       
    elif af==3:
        if l== 1 and cf== 1:
            ccaa= aaa -(aaa/50)
            return ccaa
        elif l==1 and cf==2 :
            ccab= bba -(bba/50)
            return ccab
        elif l==1 and cf == 3:
            ccac=cca -(bba/50)
            return ccac
        elif l==2 and cf==1:
           ccba=bb -(bb/50)
           return ccba
        elif l== 2 and cf==2:
            ccbb=bbb -(bbb/50)
            return ccbb
        elif l==2 and cf==3:
            ccbc=ccb -(cca/50)
            return ccbc
        elif l==3 and cf==1:
            ccca=cc -(cc/50)
            return ccca
        elif l==3 and cf == 2:
            cccb=ccb -(ccb/50)
            return cccb
        elif l==3 and cf== 3:
            cccc=ccc-(ccc/50)
            return cccc
        else:
            return "error"
       
    else:
       return "error" 
      
def c ():
    area =int(input("Enter area of your commercial plot : "))
    r= int(input("Enter rent per sq feet : "))
    mr= area *r
    return mr
if rent == 1:
   home= h()
   print(math.ceil(home))
elif rent == 2:
   viechle= v()
   print(math.ceil(viechle))
elif rent == 3:
   com=c()
   print(math.ceil(com))  
else :
    print("error")