import re
line = ("\"X\" >'Y'> I  \t> 1Z2")


def normalize(line):
    result = re.sub('[ !"$%&\'*+,-./:;<=?[\\]^`{|}~\t\n\x0b\x0c\r]', '', line)
    n = len(result)
    if result[n-1] == '>':
        result = result[:n-1]
    return result


f = normalize(line)
print(f)
