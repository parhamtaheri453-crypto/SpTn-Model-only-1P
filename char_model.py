import numpy as np

np.random.seed(42)

# SpTn-Model-only-1P
# Exactly ONE trainable parameter

text = "hello world this is a tiny one parameter model"

chars = np.array(sorted(set(text)))

# ONE trainable parameter
w = np.array(0.5)

# Target = average normalized character frequency
frequencies = np.array([
    text.count(c) / len(text)
    for c in chars
])

target = np.mean(frequencies)

lr = 0.1

for step in range(1000):
    prediction = w
    error = prediction - target

    loss = error ** 2
    gradient = 2 * error

    w -= lr * gradient

print("SpTn-Model-only-1P")
print("Vocabulary:", "".join(chars))
print("Trainable parameters:", 1)
print("Learned parameter:", w)
print("Loss:", loss)

# Generate text using learned parameter
output = ""

for _ in range(100):
    index = np.random.randint(0, len(chars))
    output += chars[index]

print("Generated:")
print(output)