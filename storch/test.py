import torch

assert torch.cuda.is_available()

print(torch.rand(3,3).cuda())