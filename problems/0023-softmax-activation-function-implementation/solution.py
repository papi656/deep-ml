import math

def softmax(scores: list[float]) -> list[float]:
    max_val = max(scores)
    s_exp = [math.exp(s - max_val) for s in scores]
    denominator = sum(s_exp)
    softmax_val = [val / denominator for val in s_exp]
    return softmax_val
    pass