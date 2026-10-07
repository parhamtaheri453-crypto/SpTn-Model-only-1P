import numpy as np

# SpTn-Model-only-1P
# Exactly ONE trainable parameter

np.random.seed(42)

# One trainable parameter
p = np.array(0.5)

# Training data
data = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

lr = 0.1

for step in range(1000):
    prediction = p
    error = prediction - np.mean(data)

    loss = error ** 2
    gradient = 2 * error

    p -= lr * gradient

# Keep probability valid
p = np.clip(p, 0.0, 1.0)

print("SpTn-Model-only-1P")
print("Trainable parameters: 1")
print("Learned probability:", p)
print("Loss:", loss)

# Generate new samples
samples = np.random.random(20) < p

print("Generated samples:")
print(samples.astype(int))