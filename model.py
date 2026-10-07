import numpy as np

# SpTn-Model-only-1P
# Exactly ONE trainable parameter

w = np.array(0.0)

x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([2.0, 4.0, 6.0, 8.0])

lr = 0.01

for step in range(1000):
    prediction = w * x
    error = prediction - y

    loss = np.mean(error ** 2)

    gradient = np.mean(2 * error * x)

    w -= lr * gradient

print("SpTn-Model-only-1P")
print("Parameter:", w)
print("Loss:", loss)
print("Prediction:", w * x)
