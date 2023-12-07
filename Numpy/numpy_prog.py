import numpy as np
list1=[[1,2,3,4],[5,6,7,8],[1,2,3,4]]
n1=np.array(list1, dtype=float)
print(n1)
print(type(n1))
print(n1.shape) #(dimension, column). y arrays of x columns
print(n1.ndim)
print(n1.dtype)

lst2=[[[1,2,3],[2],[3]],[[1],[2],[3]],[[1],[2],[3]]]
n2=np.array(lst2, dtype=object)
print(n2.shape)

lst3=[1,"s", 2]
n3=np.array(lst3)
print(type(n3))
print(n3.dtype)

n4=np.zeros((3,10), dtype=int)
print(n4)

n5=np.full((2,3),4)
print(n5)

n6=np.arange(10,20,3)
print(n6)

n7=np.random.randint(1,18,6)
print(n7)

n8=np.random.uniform(1,18,6)
print(n8)

n8_rounded=np.round(n8)
print(n8_rounded)

print(np.vstack((n8, n8_rounded, n8_rounded)))
print(np.hstack((n8, n8_rounded)))

print(np.intersect1d(n8,n8_rounded))
print(np.intersect1d(n8,n8))

print(np.setdiff1d(n8,n8_rounded))

print("Numpy Sum ",np.sum([n8,n8]))

print(n8_rounded)
print("Numpy column Sum ",np.sum([n8_rounded,n8_rounded], axis=0)) #column sum
print("Numpy row Sum ",np.sum([n8_rounded,n8_rounded], axis=1)) #row sum

print(n8_rounded +1, n8_rounded -1, n8_rounded *2, n8_rounded /2)

print(np.mean(n8_rounded))
print(np.median(n8_rounded))
print(np.var(n8_rounded))
print(np.std(n8_rounded))

#Extracting rows
lst4=[[1,2,3],[4,5,6],[7,8,9]]
n9=np.array(lst4)
print(n9[:2])

#Extracting columns
print(n9[:, 0])
print("extracting columns ", n9[:2,1])

print(n9.transpose())

np.save("numpy_file",n9)
n10=np.load("numpy_file.npy")
print(n10)

