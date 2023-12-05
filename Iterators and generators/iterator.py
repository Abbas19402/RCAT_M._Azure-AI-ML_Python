list = [1,2,3,4,5]
lst_itr = iter(list)
print("1st iteration: ")
print(next(lst_itr))
print("rest of the iteration: ")
for i in lst_itr:
    print(i)