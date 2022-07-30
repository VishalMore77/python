row = int(input("Enter No. of row :"))
cols = int(input("Enter NO. of cols :"))
num = 65
for x in range(row):
    for y in range(cols):
        data = chr(num)
        print(data,end= " ")
        num = num +1
    print()