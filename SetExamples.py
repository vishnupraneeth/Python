# Unorder collection of objects
# Set will not allow dupilicates
print("======= Declaring a set ==========")
s={10,20,30,30}
print(s,type(s))

print("====== Converting a list into set ========")

l1=[10,20,30,50,50]
s1=set(l1)
print(s1)

print("======Addition and subtaction =========")

# s1={23,32}
# w=s+s1
# print(w)
# s1[0]=10
# print(s1)

print("===== Methods of set ========")
print("add : ")
s.add(305)
print(s)

s3=s.copy()
print(s3)
print("Difference b/w s1:{10,20,30,50,50} and s3 : { 305 ,10,20,30 }" )
s5=s3.difference(s1)
s1.difference_update(s3)
print("difference " ,s5)
print("difference update " ,s1)

