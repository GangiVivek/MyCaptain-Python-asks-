lst=[];
n=0;
count =0;
n=int(input("Enter the number of elements in the list: "));
for i in range(0,n):
    print("Enter the element",i);
    m=int(input());
    lst.append(m);
print(lst);
for j in range(0,n):
    if lst[j]%2==0:
        count=count+1;
    else:
        continue;
print("The number of even numbers is :",count);
print("The number of odd numbers is :", n-count);
