def bpe_decode(ids, vocab):
    """
    Args:
        ids: list[int] - token IDs to decode
        vocab: dict[int, str] - mapping from token ID to token string
    Returns:
        str - the decoded text
    """
    tokens = []
    for id in ids:
        tokens.append(vocab[id])
    str = ''
    for token in tokens:
        if len(token.strip()) > 0 and token[0] == 'G':
            str = str + " " + token[1:]
        else:
            str = str + token
    return str
    pass