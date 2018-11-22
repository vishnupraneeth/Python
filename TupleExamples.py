print("==== Decleration of tuple ===")

t1=(10,45,50,60,60)
# t1[0]=35
# print(t1)
print(t1)
print(type(t1))
print(len(t1))
print(t1[-1])
print(t1[1:3])
print("======= Addition and Multiplication opertations on tuple")
# t3=t1+t1
# t4=t1*3
# print("Addition = " ,t3)
# print("Multiplication = " , t4)

t2=(50,70,90)
tup=t1+t1 # Addition is always done between tuples
mul=t1*3  # Multiplication is always done between tuple and integer
print("Addition of 2 tuples = ",tup )
print("Multiplication of 2 tuples = ", mul)

print("========= Tuple Methods ============")
print("count(x) method :")
t5=(10,20,30,60,70,60,70,90,100,100)
print(" occurence of element 60 is :  " , t5.count(60), "occurence of element 10 is :  ", t5.count(10))


print("Index(x) Method :")
print("Index of 100 is ", t5.index(100))

print("======= Packing and Unpacking tuple=====")
print(" PACKING A TUPLE ")
t10 = 10,20,30,40,50,60 # Packing a tuple

print(t10)

print("UNPACKING A TUPLE")

a,b,c,d,e,s=t10

print(a,b,c,d,e,type(a))

