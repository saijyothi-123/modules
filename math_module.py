# import math
# for i in dir(math):
#     print(i)
# print(dir(math))
# print(math.ceil(11.056))
# print(math.copysign(15, -8))
# print(math.fabs(-19.5))
# print(math.pow(2, 3))
# print(math.sqrt(5))
# print(math.factorial(5))
# print(math.exp(2))
# print(math.log(10))
# print(math.log(100,10))
# print(math.pi)



a = "abcdd"
b = "ac"
c = a+b
d = [*c]
print(d)
e=set(d)
print(e)
f=list(e)
print(f)
g = []
for i in f:
    # print(i)
    # print(f)
    g.append(d.count(i))
    # print(g)
k=0
for i in g:
    print(g)
#     if i%2==1:
#         k=k+1
# if k<=1:
#     print("yes")
# else:
#     print("no")