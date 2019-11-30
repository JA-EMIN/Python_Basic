def plus(*args):
    total = 0
    for n in args:
        total += n
    return total

def multiple(*args):
    total = 1
    for n in args:
        total *= n
    return total
