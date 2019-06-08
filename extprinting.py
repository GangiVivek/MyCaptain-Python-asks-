filename=input('Enter a filename: ')
value=0
for i in range(len(filename)):
    if filename[i]=='.':
       value=i
print(filename[value+1: ]);
