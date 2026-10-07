import numpy as np

# SpTn-Model-only-1P
# Text -> 1 parameter -> generated text

np.random.seed(42)

# Exactly ONE trainable parameter
w = np.float32(0.5)

text = input("Enter text: ").lower()

if not text:
    text = "hello world"

chars = np.array(list("abcdefghijklmnopqrstuvwxyz "))

# Target = average character code, normalized
codes = np.array([
    (ord(c) - 32) / 95.0
    for c in text
    if 32 <= ord(c) <= 126
])

target = np.mean(codes)

# Train ONE parameter
lr = 0.05

for step in range(1000):
    prediction = w
    error = prediction - target

    loss = error ** 2
    gradient = 2 * error

    w -= lr * gradient

print("\nSpTn-Model-only-1P")
print("Trainable parameters:", 1)
print("Parameter:", w)
print("Loss:", loss)

# Generate text
output = ""

for _ in range(200):
    value = np.random.random()

    index = int(
        np.clip(
            w * len(chars) + value * 3,
            0,
            len(chars) - 1
        )
    )

    output += chars[index]

print("\nGenerated:")
print(output)
