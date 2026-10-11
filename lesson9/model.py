
import math


def predict_probability(x, weight, bias):
    z = x * weight + bias
    return 1 / (1 + math.exp(-z))


def predict_class(probability, threshold=0.5):
    return 1 if probability >= threshold else 0
