list=[1,2,3,4,5]

# Generator object by using a generator variable
generator_valriable = (i for i in list)
print(next(generator_valriable))
print(next(generator_valriable))
print(next(generator_valriable))

# generator function uses yield keyword
def func(i):
    yield i*i

# print(func(2))
for i in range(1,10):
    print(next(func(i)))