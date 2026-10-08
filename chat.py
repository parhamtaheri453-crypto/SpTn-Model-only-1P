import numpy as np

MODEL_FILE = "sp_tn_1p.npz"

model = np.load(MODEL_FILE, allow_pickle=True)

w = float(model["w"])
vocab = [str(x) for x in model["vocab"]]

char_to_id = {c: i for i, c in enumerate(vocab)}


def logits(parameter, input_id):
    ids = np.arange(len(vocab), dtype=np.float32)
    feature = np.sin((ids + 1.0) * (input_id + 1.0))
    return parameter * feature


def softmax(values):
    values = values - np.max(values)
    exp_values = np.exp(values)
    return exp_values / np.sum(exp_values)


def next_character(previous_char):
    if previous_char not in char_to_id:
        previous_char = " "

    if previous_char not in char_to_id:
        previous_char = vocab[0]

    input_id = char_to_id[previous_char]

    probabilities = softmax(
        logits(w, input_id)
    )

    return vocab[
        np.random.choice(
            len(vocab),
            p=probabilities
        )
    ]


def generate(prompt, length=80):
    if not prompt:
        prompt = " "

    result = prompt

    previous = prompt[-1]

    for _ in range(length):
        character = next_character(previous)
        result += character
        previous = character

    return result


print("================================")
print("SpTn-Model-only-1P")
print("Trainable parameters: 1")
print("Model file:", MODEL_FILE)
print("Parameter:", w)
print("================================")
print("Type 'exit' to quit.")

while True:
    text = input("\nYou: ")

    if text.lower() == "exit":
        print("Bye.")
        break

    if not text.strip():
        continue

    print("Model:", generate(text))
