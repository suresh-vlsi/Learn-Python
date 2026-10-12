
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print("=== TECHNOLOGY STACK TEST ===")
print("Python:", sys.version.split()[0])
print("NumPy:", np.__version__)
print("Matplotlib:", matplotlib.__version__)

# Experiment data
epochs = np.arange(1, 11)
loss = np.array([
    0.95, 0.78, 0.64, 0.53, 0.44,
    0.37, 0.31, 0.27, 0.24, 0.21
])

# Basic numerical analysis
print("Number of epochs:", len(epochs))
print("Initial loss:", loss[0])
print("Final loss:", loss[-1])
print("Loss reduction:", round(loss[0] - loss[-1], 3))

# Generate and save a plot
plt.plot(epochs, loss, marker="o", label="Training loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Sample ML Training Curve")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("ml/training_loss.png", dpi=150)
print("Plot saved: ml/training_loss.png")

plt.show()
