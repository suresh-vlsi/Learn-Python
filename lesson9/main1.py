
from model import predict_probability, predict_class

weight = 1.0
bias = -1.0
x = 2.0

probability = predict_probability(x, weight, bias)
prediction = predict_class(probability)

print("Probability:", round(probability, 4))
print("Prediction:", prediction)
