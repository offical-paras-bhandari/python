  # Lambda functions or anonymous functions
# minus = lambda x,y:x-y
# print(minus(2,3))

# def a_first(a):
#     return a[1]

a = [[1,4],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)


# function inside functio
def function(n):
    return lambda x: x*n

mul = function(13)
print(mul(2))