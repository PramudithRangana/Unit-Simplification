sup_norm = {'\u2070': '0',
            '\u00b9': '1',
            '\u00b2': '2',
            '\u00b3': '3',
            '\u2074': '4',
            '\u2075': '5',
            '\u2076': '6',
            '\u2077': '7',
            '\u2078': '8',
            '\u2079': '9',
            '\u207A': '+',
            '\u207B': '-'}

norm_sup = {'0': '\u2070',
            '1': '\u00b9',
            '2': '\u00b2',
            '3': '\u00b3',
            '4': '\u2074',
            '5': '\u2075',
            '6': '\u2076',
            '7': '\u2077',
            '8': '\u2078',
            '9': '\u2079',
            '+': '\u207A',
            '-': '\u207B'}

ls = []


def supScr_to_norm(indices):
    for i in str(indices):
        r = '{}'.format(sup_norm.get(i))
        ls.append(r)
    result = ''.join([i for i in ls])
    ls.clear()
    return str(result)


def norm_to_supScr(indices):
    for i in str(indices):
        r = '{}'.format(norm_sup.get(i))
        ls.append(r)
    result = ''.join([i for i in ls])
    ls.clear()
    return str(result)
