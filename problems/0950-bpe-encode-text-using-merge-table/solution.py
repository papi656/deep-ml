def bpe_encode(text, token_to_id, merges):
    # Your code here
    if len(text.strip()) == 0:
        return []

    tokens = []
    for char in text:
        tokens.append(token_to_id[char])
    
    for i in range(0,len(tokens)):
        best_pair = None
        best_rank = float('inf')
        for j in range(0, len(tokens)-1):
            try:
                if merges[(tokens[j], tokens[j+1])] < best_rank:
                    best_pair = (tokens[j], tokens[j+1])
                    best_rank = merges[(tokens[j], tokens[j+1])]
            except:
                pass
        new_tokens = []
        if best_pair:
            skip_next = False
            for j in range(0, len(tokens)-1):
                if skip_next:
                    skip_next = False
                    continue
                if best_pair == (tokens[j], tokens[j+1]):
                    new_tokens.append(best_rank)
                    skip_next = True
                else:
                    new_tokens.append(tokens[j])
            if skip_next == False:
                new_tokens.append(tokens[-1])
        else:
            break
        
        tokens = new_tokens
    return tokens
    pass