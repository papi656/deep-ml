def build_vocab(tokens):
    """
    Build a vocabulary dictionary from a list of tokens.

    Args:
        tokens: list of string tokens

    Returns:
        Dict mapping each unique token (sorted) to a unique integer ID starting from 0.
    """
    unique_tokens = set()
    for t in tokens:
        unique_tokens.add(t)
    vocab = dict()
    sorted_tokens = sorted(unique_tokens)
    for pos, t in enumerate(sorted_tokens):
        vocab[t] = pos
    return vocab
    pass
