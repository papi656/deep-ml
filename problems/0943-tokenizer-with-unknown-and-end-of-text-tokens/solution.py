import re

def tokenize(vocab, text, mode):
    """
    vocab: dict[str, int] containing '<|unk|>' and '<|endoftext|>'
    text: str (if mode='encode') or list[int] (if mode='decode')
    mode: 'encode' or 'decode'
    """
    if mode == 'encode':
        tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        tokens = [token for token in tokens if len(token.strip()) > 0]
        encoded = []
        for token in tokens:
            try:
                encoded.append(vocab[token])
            except:
                encoded.append(vocab["<|unk|>"])
        return encoded
    else:
        reverse_vocab = dict()
        for k, v in vocab.items():
            reverse_vocab[v] = k
        simple_text = []
        for id in text:
            simple_text.append(reverse_vocab[id])
        # combine
        decoded = ""
        for i in range(len(simple_text)):
            if i == 0:
                decoded = simple_text[i]
            else:
                decoded = decoded + " " + simple_text[i]

        pattern = r"""\s+([,.?!"()':;])"""
        return re.sub(pattern, r"\1", decoded)




    pass