import numpy as np

MODEL_FILE = "sp_tn_1p.npz"

model = np.load(MODEL_FILE)
w = float(model["w"])

# Fixed generation tables.
# These are NOT trainable parameters.
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

clusters = [
    "br", "cr", "dr", "fr", "gr", "kr", "pr", "tr",
    "bl", "cl", "fl", "gl", "pl",
    "sk", "sl", "sm", "sn", "sp", "st", "sw",
    "vr", "zh"
]

endings = [
    "n", "r", "s", "t", "l", "m", "k",
    "x", "d", "v"
]

punctuation = ["", "", "", ".", "!", "?", ","]

print("================================")
print("SpTn-Model-only-1P")
print("Trainable parameters: 1")
print("Model file:", MODEL_FILE)
print("Parameter:", w)
print("Type 'exit' to quit")
print("================================")


def choose_without_repeat(pool, used):
    available = [c for c in pool if c not in used]

    if not available:
        return None

    return available[int(np.random.random() * len(available))]


def make_word():
    # Different word lengths.
    length = int(4 + np.random.random() * 7)

    used = set()
    word = ""

    # Sometimes start with a consonant cluster.
    if np.random.random() < 0.35:
        cluster = clusters[int(np.random.random() * len(clusters))]

        for c in cluster:
            if c not in used:
                word += c
                used.add(c)

    while len(word) < length:
        # Alternate consonant/vowel patterns.
        if len(word) % 2 == 0:
            c = choose_without_repeat(consonants, used)
        else:
            c = choose_without_repeat(vowels, used)

        if c is None:
            break

        word += c
        used.add(c)

    # Optional final consonant.
    if len(word) < length and np.random.random() < 0.5:
        c = choose_without_repeat(endings, used)

        if c is not None:
            word += c
            used.add(c)

    return word


def generate_sentence(text):
    # The single trainable parameter affects generation.
    # Everything else is fixed generation logic.
    seed_shift = int(abs(w) * 1000)

    # Input affects the deterministic seed without becoming a parameter.
    text_value = sum(ord(c) for c in text)

    np.random.seed(seed_shift + text_value)

    # 7–13 unique words.
    word_count = int(7 + np.random.random() * 7)

    words = []
    seen = set()

    attempts = 0

    while len(words) < word_count and attempts < 100:
        word = make_word()
        attempts += 1

        if word and word not in seen:
            words.append(word)
            seen.add(word)

    # Random punctuation and capitalization.
    result = []

    for i, word in enumerate(words):
        if np.random.random() < 0.18:
            word = word.capitalize()

        result.append(word)

    sentence = " ".join(result)

    punctuation_mark = punctuation[
        int(np.random.random() * len(punctuation))
    ]

    return sentence + punctuation_mark


while True:
    text = input("\nYou: ")

    if text.lower() == "exit":
        print("Bye.")
        break

    if not text.strip():
        continue

    print("Model:", generate_sentence(text))
