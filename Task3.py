#using functions
#input list of words
#output length of the longest word
lst=[];
def length():
    i=0;
    n=0;
    m=0;
    i=int(input("Enter the number of words you are interested to input: "));
    for j in range(0,i):
        print("Enter the word",j);
        ele=input();
        lst.append(ele);
        m=len(ele);
        if(m>n):
            n=m;
    print("The length of the longest word is :", n);

length();
print("The words given by are :", lst);

