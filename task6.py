s1=0;
s2=0;
s3=0;
s1=input("Enter the lenght of side one of the triangle :");
s2=input("Enter the lenght of side two of the triangle :");
s3=input("Enter the lenght of side three of the triangle :");

if s1==s2:
    if s2==s3:
        print("This is an Equilateral triangle");
    else:
        print("This is a Isoceles triangle");
elif s2==s3:
    if s3==s1:
        print("This is an Equilateral triangle");
    else:
        print("This is an Isoceles triangle");

elif s3==s1:
    if s3==s2:
        print("This is a equilateral triangle");
    else:
        print("This is a Iscoceles triangle");
else:
    print("This is a scalene triangle");

        
