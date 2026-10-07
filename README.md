# SpTn-Model-only-1P

An experimental generative model with exactly **1 trainable parameter**.

## Goal

The goal of SpTn-Model-only-1P is to explore how much generative behavior can be achieved with an extremely small number of trainable parameters.

## Current Version

- Trainable parameters: **1**
- Parameter type: `float32`
- Raw parameter storage: **4 bytes**
- Framework: **NumPy**
- Training: From scratch
- Generation benchmark: **10,000 characters**
- Measured generation speed: **76,726 characters/second**

## Experiments

The project contains several experiments exploring:

- One-parameter training
- Character generation
- Text generation
- Parameter capacity
- Generation speed
- Extremely small model storage

## Important Note

This is an experimental project and is **not a competitive language model**.

The purpose is to investigate the practical limits of a model with only one trainable parameter.

## Roadmap

SpTn is planned as a parameter-scaling experiment:

```text
1P
↓
100P
↓
1K
↓
10K
↓
100K
↓
1M
↓
10M

## Interactive Chat

Run the experimental one-parameter chat:

    python chat.py

Type your message after `You:`.

Type `exit` to quit.
