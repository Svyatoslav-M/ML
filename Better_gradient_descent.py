import torch

x = torch.tensor(
    [8., 8.], requires_grad=True)

optimizer = torch.optim.SGD([x], lr=0.001)

def function_parabola(variable):
    return 10 * (variable ** 2).sum()

def make_gradient_step(function, variable):
    function_result = function(variable)
    function_result.backward()
    optimizer.step()
    optimizer.zero_grad()
    
for i in range(500):
    make_gradient_step(function_parabola, x)

print(x.grad)
