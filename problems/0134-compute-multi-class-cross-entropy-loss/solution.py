import torch

def compute_cross_entropy_loss(predicted_probs: torch.Tensor, true_labels: torch.Tensor, epsilon: float = 1e-15) -> float:
    """Compute average cross-entropy loss for multi-class classification.
    
    Args:
        predicted_probs: Tensor of predicted probabilities (batch_size, num_classes)
        true_labels: One-hot encoded true labels (batch_size, num_classes)
        epsilon: Small value for numerical stability
    
    Returns:
        Average cross-entropy loss as a float
    """
    clamped = torch.max(predicted_probs, torch.tensor(epsilon))
    loss = - (true_labels * torch.log(clamped)).sum(dim=1).mean()
    return loss.item()
    pass