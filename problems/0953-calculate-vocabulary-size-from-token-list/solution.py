def vocab_size(tokens, special_tokens=None):
    """Return the vocabulary size from a list of preprocessed tokens.

    Args:
        tokens: list[str] of preprocessed tokens
        special_tokens: optional list[str] of special tokens to include
    Returns:
        int: number of unique tokens in the combined vocabulary
    """
    vocab = set()
    for token in tokens:
        vocab.add(token)
    if special_tokens:
        for s in special_tokens:
            vocab.add(s)
    return len(vocab)
    pass