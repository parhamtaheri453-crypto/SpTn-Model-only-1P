import numpy as np

np.random.seed(42)

# SpTn-Model-only-1P
# Exactly ONE trainable parameter

w = np.float32(0.5)

chars = np.array(list("abcdefghijklmnopqrstuvwxyz "))

print("================================")
print("SpTn-Model-only-1P")
print("Trainable parameters: 1")
print("Type 'exit' to quit")
print("================================")

while True:
    text = input("\nYou: ")

    if text.lower() == "exit":
        print("Bye.")
        break

    if not text:
        continue

    codes = np.array([
        (ord(c) - 32) / 95.0
        for c in text
        if 32 <= ord(c) <= 126
    ])

    if len(codes) == 0:
        print("Model: Please enter ASCII text.")
        continue

    target = np.mean(codes)

    # Train the single parameter
    for _ in range(1000):
        error = w - target
        gradient = 2 * error
        w -= np.float32(0.05 * gradient)

    w = np.clip(w, 0.0, 1.0)

    output = ""

    for _ in range(100):
        value = np.random.random()

        index = int(
            np.clip(
                w * len(chars) + value * 3,
                0,
                len(chars) - 1
            )
        )

        output += chars[index]

    print("Model:", output)
    print("Parameter:", float(w))
