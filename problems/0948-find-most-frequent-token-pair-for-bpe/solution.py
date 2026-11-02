def most_frequent_pair(sequences):
    """
    Args:
        sequences: list[list[int]] - list of token ID sequences
    Returns:
        tuple(int, int) or None - the most frequent adjacent pair, with ties
        broken by first appearance. Returns None if no pair exists.
    """
    count = dict()
    max_count = 0
    res = None
    for sequence in sequences:
        for i in range(0, len(sequence)-1):
            key = str(sequence[i]) + "-" + str(sequence[i+1])
            try:
                count[key] += 1
                if max_count < count[key]:
                    max_count = count[key]
                    res = (sequence[i], sequence[i+1])
            except:
                count[key] = 1
                if max_count < count[key]:
                    max_count = count[key]
                    res = (sequence[i], sequence[i+1])
    return res
    pass