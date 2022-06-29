mynum = int(input("Type i number: "))
start = 0
end = int(input("Type the end: "))
for x in range(start,end):
    if x%mynum == 0 :
        print(x)