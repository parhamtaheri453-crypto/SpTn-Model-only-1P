import numpy as np

model = np.load("sp_tn_1p.npz")

w = model["w"]

print("SpTn-Model-only-1P")
print("Trainable parameters: 1")
print("Parameter:", float(w))
print("Model loaded successfully.")
