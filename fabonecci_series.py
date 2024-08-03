nterms=10
n1=0
n2=1
count=2
if nterms <=0:
    print('enter positive num:')
elif nterms == 1:
    print("fibonacci series upto",nterms,":")
    print(n1)
else:
    
    print("fibonacci series upto",nterms,":")
    print(n1,":",n2,end =' ,')
    while count < nterms:
        nth = n1+n2
        print(nth,end =' ,')
        n1 =n2 
        n2 =nth
        count +=1
