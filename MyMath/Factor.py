def Factor(nNumber):
    # # long code
    # rst = []
    # for n in range(1, nNumber+1):
    #     if nNumber % n is 0:
    #         rst.append(n)
    # return rst

    # # shor code
    return [n for n in range(1, 1+nNumber) if nNumber % n is 0]