import numpy as np

# SpTn-Model-only-1P
# Capacity experiment

print("================================")
print("SpTn-Model-only-1P")
print("Capacity Test")
print("================================")

# Exactly ONE parameter
w = np.float32(0.5)

values = np.linspace(0.0, 1.0, 1000001, dtype=np.float32)

# Find how many distinct float32 values are representable
unique_count = len(np.unique(values))

print("Trainable parameters:", 1)
print("Parameter dtype:", w.dtype)
print("Parameter size:", w.nbytes, "bytes")
print("Distinct tested values:", unique_count)

# Information capacity approximation
bits = np.log2(unique_count)

print("Approximate information capacity:")
print(bits, "bits")

print("================================")