l1=[10,20,30,40]
l1.append(40)
print(l1)
print("appending one list to another list")
l2=[300,400,500]
l1.append(l2)
print("append=",l1)
print("----------------------","ExtendMethod","----------------")
l2=[300,400,500]
l1.extend(l2)
print(l1)

l3=[10,20]

l2.extend(l3)
print(l2)

print("-------------","Insert Method ","-----------")
l4=[324,675,-1,-2]
l4.insert(4,30)
print("Inserting ", l4)
print("Index of -2 number =",l4.index(-2))

print("============== sorting l1 ==========")
l4.sort()
print(l4)

l4[0]=35
print(l4)
