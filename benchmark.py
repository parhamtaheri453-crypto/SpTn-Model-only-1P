import numpy as np
import time
import os

np.random.seed(42)

# ==================================================
# SpTn-Model-only-1P Benchmark
# ==================================================

PARAMETERS = 1

# Exactly ONE trainable parameter
w = np.array(0.3430751356845402)

text = "hello world this is SpTn model only one parameter"

chars = np.array(list("abcdefghijklmnopqrstuvwxyz "))

start = time.perf_counter()

output = ""

for _ in range(10000):
    index = np.random.randint(0, len(chars))
    output += chars[index]

elapsed = time.perf_counter() - start

print("================================")
print("SpTn-Model-only-1P")
print("================================")

print("Trainable parameters:", PARAMETERS)
print("Parameter value:", w)
print("Characters generated:", len(output))
print("Generation time:", elapsed, "seconds")
print("Characters / second:", len(output) / elapsed)

model_size = PARAMETERS * 8

print("Raw parameter size:", model_size, "bytes")
print("================================")

with open("generated_10000.txt", "w") as f:
    f.write(output)

print("Saved: generated_10000.txt")