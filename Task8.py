lst=[];
n=0;
p=1;
n=int(input("Enter the number of elements in the list: "));
for i in range(0,n):
    print("Enter the element",i);
    m=int(input());
    p=p*m;
    lst.append(m);
print(lst);
print("The product of the elements in the list is",p);
          
          
