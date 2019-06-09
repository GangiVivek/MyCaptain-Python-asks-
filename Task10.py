class rectangle:
    lenght=0;
    width=0;
    def area(self):
        length=int(input("Enter the length of the rectange: "));
        width=int(input("Enter the width of the rectangle: "));
        a=length*width;
        print("The area of the rectangle is: ",a);
        return;
rect1=rectangle();
rectangle.area(rect1);
                   
