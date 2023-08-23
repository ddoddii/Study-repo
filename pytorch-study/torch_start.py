import torch 

my_tensor = torch.tensor([[1,2,3],[4,5,6]], dtype = torch.float32, device = "mps:0")
print(my_tensor)
print(my_tensor.shape)

x = torch.empty(size=(3,3))
x = torch.rand((3,3))
x = torch.eye(5,5)
print(x)