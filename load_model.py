import numpy as np

MODEL_FILE = "sp_tn_1p.npz"

model = np.load(MODEL_FILE, allow_pickle=True)

w = model["w"]
vocab = model["vocab"]

print("SpTn-Model-only-1P")
print("Trainable parameters: 1")
print("Parameter:", float(w))
print("Vocabulary size:", len(vocab))
print("Model loaded successfully.")
