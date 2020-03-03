def func1(a):
    return None

def func2(a):
    return func1(a) * func1(a)

#print (func2(2))



list = [x * x for x in range(5)]

def fun(lst):
    del lst[list[2]]
    return lst

print (fun(list))


#############################
def func(a,b):
    return b ** a

#print (func(b=2 , 2))

#############################

x = 1//5 + 1 / 5

print (x)


##########################

print ('line 35')
def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x,y-1)

print (func(0,3))


print ('line 45')


def funx(inp=2,out=3):
    return inp * out


print (funx(out=2))


x = 3
y = 2

x = x % y
x = x % y
y =  y % x
print (y)



lst = [[x for x in range(3)] for  y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print ("#")


z = 0

y = 10

x = y < z and z > y or y > z and z < y

print (x)