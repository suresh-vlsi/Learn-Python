
import torch

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

# y = wx + b
x = torch.tensor([1.0, 2.0, 3.0])
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)

y = w * x + b
loss = y.mean()

loss.backward()

print("Predicted values:", y.detach().tolist())
print("Mean output:", loss.item())
print("Gradient of w:", w.grad.item())
print("Gradient of b:", b.grad.item())
