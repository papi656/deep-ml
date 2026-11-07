import torch

def byte_pair_encoding(corpus: dict, num_merges: int) -> list:
    """
    Train a BPE tokenizer on the given corpus using PyTorch for pair counting.
    
    Args:
        corpus: Dictionary mapping space-separated token sequences to their frequencies.
                Example: {"l o w </w>": 5, "n e w </w>": 6}
        num_merges: Number of merge operations to perform.
    
    Returns:
        List of tuples, where each tuple contains the two tokens that were merged.
        Example: [('l', 'o'), ('lo', 'w')]
    """
    pair_count = dict()
    for key, value in corpus.items():
        tokens_per_key = key.split()
        for i in range(0, len(tokens_per_key)-1):
            try:
                pair_count[(tokens_per_key[i], tokens_per_key[i+1])] += value
            except:
                pair_count[(tokens_per_key[i], tokens_per_key[i+1])] = value
    
    merge_pair = []
    while num_merges > 0:
        # find most frequent pair
        most_pair = None
        most_count = 0
        for key, value in pair_count.items():
            if value > most_count:
                most_pair = key
                most_count = value

        if len(pair_count) == 1:
            break

        pair_count.pop(most_pair)
        merge_pair.append(most_pair)
        temp_pair = dict(pair_count)
        for key, value in pair_count.items():
            if key[0] == most_pair[1] or most_pair[0] == key[1]:
                s = most_pair[0] + most_pair[1]
                if key[0] == most_pair[1]:
                    temp_pair[(s, key[1])] = value
                else:
                    temp_pair[(key[0], s)] = value
                temp_pair.pop(key)
            else:
                temp_pair[key] = value

        pair_count = temp_pair
        num_merges -= 1

    return merge_pair

    pass
