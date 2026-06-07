import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

# Parameters
N = 1000
dt = 0.01
t = np.arange(N) * dt

# True motion: constant velocity
x0 = 0.0
v = 2.0
x_true = x0 + v * t

# Noisy measurement
sigma = 1.0
noise = sigma * np.random.randn(N)
x_measured = x_true + noise

# Measurement error
error = x_measured - x_true

# Plot true vs measured
plt.figure(figsize=(10, 4))
plt.plot(t, x_true, label="True position")
plt.scatter(t, x_measured, s=5, label="Noisy measurement")
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("True Position vs Noisy Measurement")
plt.grid(True)
plt.legend()
plt.savefig("plots/noisy_measurement.png")
plt.show()

# Plot error over time
plt.figure(figsize=(10, 4))
plt.plot(t, error)
plt.xlabel("Time")
plt.ylabel("Measurement error")
plt.title("Measurement Error Over Time")
plt.grid(True)
plt.savefig("plots/measurement_error.png")
plt.show()

# Histogram of error
plt.figure(figsize=(8, 4))
plt.hist(error, bins=40)
plt.xlabel("Error")
plt.ylabel("Frequency")
plt.title("Measurement Error Histogram")
plt.grid(True)
plt.savefig("plots/error_histogram.png")
plt.show()

print("Error mean:", np.mean(error))
print("Error variance:", np.var(error))
print("Error standard deviation:", np.std(error))