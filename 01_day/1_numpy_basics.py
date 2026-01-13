import numpy as np

arr = np.array([1,2,3,4,5])

print("Array:", arr)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())

a = np.array([1,2,3])
b = np.array([10,20,30])

print("Addition:", a + b)
print("Multiplication:", a * b)

matrix = np.array([[1,2,3], [4,5,6]])
print("Shape:", matrix.shape)
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
