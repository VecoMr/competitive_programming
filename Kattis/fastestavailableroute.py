a,*l=open(0)
print(f"Your destination will arrive in {(sum(i.count('.')for i in l)+1)*int(a.split()[2])} meters")