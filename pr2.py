import numpy as np 

# initializing an array
a = np.array([1,2,3])
# initializing a matrix
b = np.array([
    [1,2],
    [3,4]
])
# initializing a tensor
c = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
#getting shape of the array
a.shape #(3,) , (2,2), (2,2,2)
#and it's dimension
a.ndim  #i , 2, ...

# fill a shape with 1, 0 or numbers
np.ones((2,2)) , np.zeros(2), np.full(2, 1.23)

np.arange(start=0, end=3, step=1)
np.linspace(start=1, end=3, how_many=3)

rng =np.random.default_rng()
rng.random((3,2))

np.random.rand(2)  #more problematic


# in torch
import torch
na = np.zeros(3)
torch_tensor = torch.tensor(na) #tensor is a fancy word for array
torch.tensor([1,2])
torch.rand(size=4, out=3, dtype=torch.float32)
torch.to(torch.float16)

# in case sytem doesnt have gpu:
if torch.cuda.is_available():
    tensor = torch.tensor([1,2,3]).to('cuda')   #only fpr gpu: .to('cuda')
else:
    tensor = torch.tensor([1,2,3])


#put two array on top of each other
v1= np.ones(3) 
v2 = torch.ones(3)
np.stack((v1, v2))
torch.stack((v1, v2)).shape

np.concatenate((v1, v2))
