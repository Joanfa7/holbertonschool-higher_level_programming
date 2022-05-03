#!/use/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char1 = sentence[0]
    if length == 0:
        return None
    else:
        return [length, char1]
