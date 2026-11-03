def replace_pair(sequences, pair, new_id):
    # Your code here
    replaced = []
    for sequence in sequences:
        curr_sequence = []
        skip_next = False
        for i in range(0, len(sequence)-1):
            if skip_next:
                skip_next = False
                continue
            if (sequence[i], sequence[i+1]) == pair:
                curr_sequence.append(new_id)
                skip_next = True
            else:
                curr_sequence.append(sequence[i])
        if not skip_next and len(sequence):
            curr_sequence.append(sequence[-1])
        replaced.append(curr_sequence)

    return replaced
            
    pass