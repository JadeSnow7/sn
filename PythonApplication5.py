import torch
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
a = torch.arange(3).reshape((3, 1))
b = torch.arange(4).reshape((1, 4))
'''
Z = torch.zeros_like(Y)

print('id(Z):', id(Z))
Z[:] = X + Y
print('id(Z):', id(Z))
before = id(X)
X += Y
print(id(X) == before)
'''
A = X.numpy()
B = torch.tensor(A)

a = torch.tensor([3.5])

m=torch.tensor([1,2,3,4]).reshape((1,1,4))
n=torch.ones(4).reshape((2,2,1))

print(m,'\n',n,'\n',m+n)

