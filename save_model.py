import numpy as np

# SpTn-Model-only-1P
# Exactly ONE trainable parameter

# The single parameter represents the center of a character distribution.
w = np.array(0.5, dtype=np.float32)

# Training data: normalized character positions.
data = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90],
                dtype=np.float32)

lr = 0.01

for _ in range(1000):
    error = w - np.mean(data)
    gradient = 2 * error
    w -= lr * gradient

np.savez(
    "sp_tn_1p.npz",
    w=w,
)

print("Model saved.")
print("Trainable parameters:", 1)
print("Parameter:", float(w))
