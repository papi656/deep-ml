import re

def encode(text, vocab):
    tokenized = re.split(r"([,.:;?_!\"()']|--|\s)", text)
    final_tokens = [token for token in tokenized if len(token.strip()) > 0]
    encoding = []
    for token in final_tokens:
        encoding.append(vocab[token])
    return encoding
    pass

def decode(ids, vocab):
    reverse_vocab = dict()
    for key, value in vocab.items():
        reverse_vocab[value] = key
    decoded = []
    for id in ids:
        decoded.append(reverse_vocab[id])
    str = ""
    for d in decoded:
        if len(str):
            str = str + " " + d
        else:
            str = d
    pattern = r"""\s+([,.?!"()'])"""
    return re.sub(pattern, r"\1", str)
    
    pass