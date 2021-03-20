def my_sum(*integers):
    result=0
    for x in integers:
        result+=x
    return result

print(my_sum(1,2,3))

#Bear in mind that the iterable object
#you’ll get using the unpacking operator * is not a list but a tuple.

def concate(**kwargs):
    result=""
    for arg in kwargs.values():
        result=result+arg
    return result

# what if you want to create a function
#that takes a changeable number of both positional and named arguments?

a,*b,c=[1,2,3,4,]

first=[1,2,3]
second=[3,2,1]
