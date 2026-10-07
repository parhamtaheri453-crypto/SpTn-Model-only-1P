import numpy as np

# SpTn-Model-only-1P
# A 1-parameter generative model

np.random.seed(42)

# The only trainable parameter
w = np.array(0.5)

# Training data: probabilities we want to approximate
data = np.array([0.1, 0.2, 0.3, 0.4])

learning_rate = 0.1

for step in range(1000):
    prediction = w * data

    loss = np.mean((prediction - data) ** 2)

    gradient = np.mean(2 * (prediction - data) * data)

    w -= learning_rate * gradient

print("SpTn-Model-only-1P")
print("Trainable parameters: 1")
print("Learned parameter:", w)
print("Loss:", loss)

# Generation
random_value = np.random.random()
generated = w * random_value

print("Random input:", random_value)
print("Generated value:", generated)