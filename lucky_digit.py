import pdb
pdb.set_trace()
temp=int(input("input the number : "))
a=0
while temp!=0:
    
    
        a=a+ temp%10
        temp=temp//10
        if a>9 and temp==0:
         temp=a
         a=0
    

print(a)