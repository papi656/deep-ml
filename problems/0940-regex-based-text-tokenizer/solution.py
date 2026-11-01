import re

def tokenize_text(text: str) -> list:
    """
    Split raw text into tokens using regex-based splitting on whitespace
    and punctuation. Returns a list of non-empty stripped tokens.
    """
    by_space = text.split()
    punctuations_pattern = "(--|[,.:;?_!\"()'])"
    after_puntuation_split = []
    for word in by_space:
        tmp = re.split(punctuations_pattern, word)
        for t in tmp:
            if len(t):
                after_puntuation_split.append(t)
    
    return after_puntuation_split
    pass