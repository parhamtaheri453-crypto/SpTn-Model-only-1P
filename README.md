---
tags:
- experimental
- generative-model
- one-parameter
- research
- toy-model
library_name: numpy
---

# SpTn-Model-only-1P

A minimal experimental generative model with exactly **1 trainable parameter**.

SpTn-Model-only-1P explores how much generative behavior can be produced under an extreme one-parameter constraint.

## Model

- **Trainable parameters:** 1
- **Parameter type:** float32
- **Architecture:** Character-level generative model
- **Framework:** NumPy
- **Model file:** `sp_tn_1p.npz`
- **Status:** Experimental
- **Language understanding:** No

## How It Works

The model contains exactly one trainable parameter: `w`.

The parameter is trained using gradient descent.

During generation:

**Input character → Fixed feature function → w → Character probabilities → Generated character**

The generated text is produced directly from the trained parameter through the model's probability calculation.

The vocabulary and feature function are fixed and are not trainable parameters.

## Download

### Hugging Face

Download the model directly:

```bash
wget "https://huggingface.co/KtiyaKK/SpTn-Model-only-1P/resolve/main/sp_tn_1p.npz?download=true"

Download chat.py:

wget "https://raw.githubusercontent.com/parhamtaheri453-crypto/SpTn-Model-only-1P/main/chat.py"

Then run:

python chat.py

GitHub

Download the repository or the required files from GitHub.

No Git installation is required if the files are downloaded manually.

Installation

Install NumPy:

pip install numpy

Quick Start

Download these two files:

- sp_tn_1p.npz
- chat.py

Place them in the same directory.

Run:

python chat.py

Example:

You: hello
Model: helloenemts aonddsoc xroxoe exhxnyyscdlhoahmtlnphlmwxypo

The generated text is experimental and is not intended to be meaningful natural language.

Load the Model

To verify and load the model:

python load_model.py

Expected output:

SpTn-Model-only-1P
Trainable parameters: 1
Parameter: ...
Vocabulary size: ...
Model loaded successfully.

Training

The model can be trained with:

python save_model.py

This trains the single parameter and saves the resulting model to:

sp_tn_1p.npz

Architecture

SpTn-Model-only-1P contains exactly one trainable scalar: w.

The model uses a fixed character vocabulary and a fixed feature function.

Only w is updated during training.

The generation process uses the trained value of w to calculate character probabilities.

Important Limitations

SpTn-Model-only-1P is an experimental research project.

It is not a general-purpose language model.

The model does not understand natural language or the semantic meaning of the user's input.

Its output is character-level synthetic text.

The extremely small parameter count severely limits the model's capacity.

The project is intended to explore parameter efficiency and extremely low-parameter generative systems.

Roadmap

The project will investigate progressively larger parameter counts:

1P → 100P → 1K → 10K → 100K → 1M → 10M

The goal is to study how generative behavior changes as the number of trainable parameters increases.

Repository

GitHub: https://github.com/parhamtaheri453-crypto/SpTn-Model-only-1P

Hugging Face: https://huggingface.co/KtiyaKK/SpTn-Model-only-1P

Disclaimer

SpTn-Model-only-1P is an experimental project.

It should not be compared directly with modern large language models.

The project is intended for experimentation, education, and research into extremely low-parameter generative models.
