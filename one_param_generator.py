import numpy as np

np.random.seed(42)

# SpTn-Model-only-1P
# Exactly ONE trainable parameter

w = np.array(0.5)

text = "hello world this is a one parameter model"

chars = np.array(list("abcdefghijklmnopqrstuvwxyz "))

# Training target:
# frequency of letters in the text
counts = np.array([text.count(c) for c in chars], dtype=float)
target = counts / counts.sum()

# One parameter controls the sharpness of the distribution
lr = 0.01

for step in range(1000):
    temperature = np.exp(w)

    logits = np.log(target + 1e-8) / temperature
    probs = np.exp(logits - np.max(logits))
    probs /= probs.sum()

    loss = -np.sum(target * np.log(probs + 1e-8))

    gradient = 0.01 * (loss - 1.0)
    w -= lr * gradient

print("SpTn-Model-only-1P")
print("Trainable parameters:", 1)
print("Parameter:", w)
print("Loss:", loss)

temperature = np.exp(w)

logits = np.log(target + 1e-8) / temperature
probs = np.exp(logits - np.max(logits))
probs /= probs.sum()

output = ""

for _ in range(200):
    output += np.random.choice(chars, p=probs)

print("\nGenerated:")
print(output)
with open("generated.txt", "w") as f:
    f.write(output)

print("\nCharacters generated:", len(output))
print("File: generated.txt")
