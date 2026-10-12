
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Two features per sample
X = np.array([
    [1.0, 1.0],
    [1.5, 1.0],
    [2.0, 1.5],
    [7.0, 7.0],
    [8.0, 7.0],
    [9.0, 8.0]
])

y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

predictions = model.predict(X)
probabilities = model.predict_proba(X)

print("Predictions:", predictions)
print("Training accuracy:", accuracy_score(y, predictions))
print("First sample probabilities:", probabilities[0])
