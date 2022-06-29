list1 = []
list2 = []
start = int(input("the numbert Start on: "))
end = int(input("the number end on: "))
for x in range(start,end):
    if x%2 == 0:
        list1.append(x)
    elif x%2 != 0:
        list2.append(x)
print(f"Even list: {list1}")
print(f"odd list: {list2}")