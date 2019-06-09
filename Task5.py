#input month name
#print numbe of days in the month

lst1=["jan","feb","mar","apr","may","jun","july"];
lst2=["aug","sep","oct","nov","dec",0,0];
month=str(input("Enter the month to find the number of days :"));
print("The number of days in this month is :");
for i in range(0,len(lst1)):
    if month==lst1[i] and i%2==0:
        print("31");
    elif month==lst2[i] and i%2==0:
        print("31");
    elif month==lst1[i] or month==lst2[i]:
        print("30");
    else:
        continue;
    

