import torch

def entropy_and_cross_entropy(P: torch.Tensor, Q: torch.Tensor) -> tuple[float, float]:
    """
    Compute entropy of P and cross-entropy between P and Q.
    
    Args:
        P: True probability distribution (torch.Tensor)
        Q: Predicted probability distribution (torch.Tensor)
    
    Returns:
        Tuple of (entropy H(P), cross-entropy H(P,Q))
    """
    # entropy
    entropy = - torch.special.xlogy(P, P).sum()
    cross_entropy = - torch.special.xlogy(P, Q).sum()
    return entropy.item(), cross_entropy.item()
    pass