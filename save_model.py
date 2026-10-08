import numpy as np

# SpTn-Model-only-1P
# Exactly ONE trainable parameter.

MODEL_FILE = "sp_tn_1p.npz"

# Fixed training corpus.
# These are data, not trainable parameters.
text = """
hello world
this is a tiny experimental model
sp tn one parameter
research experiment
hello model
"""

# Fixed vocabulary.
# These values are NOT trainable parameters.
vocab = sorted(set(text))
char_to_id = {c: i for i, c in enumerate(vocab)}

# Training examples: previous character -> next character.
pairs = []

for i in range(len(text) - 1):
    x = text[i]
    y = text[i + 1]
    pairs.append((char_to_id[x], char_to_id[y]))

# Exactly ONE trainable parameter.
w = np.array(0.5, dtype=np.float32)

learning_rate = 0.05
steps = 5000


def logits(parameter, input_id):
    """
    Fixed feature function.
    The only trainable value is `parameter`.
    """
    n = len(vocab)

    ids = np.arange(n, dtype=np.float32)

    # Fixed features.
    # No trainable weights here.
    feature = np.sin((ids + 1.0) * (input_id + 1.0))

    return parameter * feature


def softmax(values):
    values = values - np.max(values)
    exp_values = np.exp(values)
    return exp_values / np.sum(exp_values)


for step in range(steps):
    total_loss = 0.0
    total_gradient = 0.0

    for input_id, target_id in pairs:
        z = logits(w, input_id)
        probabilities = softmax(z)

        loss = -np.log(probabilities[target_id] + 1e-12)
        total_loss += loss

        ids = np.arange(len(vocab), dtype=np.float32)
        feature = np.sin((ids + 1.0) * (input_id + 1.0))

        expected_feature = np.sum(probabilities * feature)
        gradient = expected_feature - feature[target_id]

        total_gradient += gradient

    total_gradient /= len(pairs)

    w -= learning_rate * total_gradient

    if step % 500 == 0:
        average_loss = total_loss / len(pairs)
        print(
            f"step={step} "
            f"loss={average_loss:.6f} "
            f"w={float(w):.6f}"
        )


np.savez(
    MODEL_FILE,
    w=w,
    vocab=np.array(vocab),
)

print()
print("SpTn-Model-only-1P")
print("Model saved:", MODEL_FILE)
print("Trainable parameters:", 1)
print("Parameter:", float(w))
print("Final loss:", float(total_loss / len(pairs)))
