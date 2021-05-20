# python
# bruteforce substring search. returns true if match somewhere in string, else False
def contains(txt, pat):
    n = len(txt)
    m = len(pat)

    for i in range(n-m):  # index of each character in text string
        for j in range(m):  # forward search for each chracter in pattern string
            if txt[i+j] != pat[j]:  # break (and go the next c) if mismatch
                break
            # continue until the entire pattern string has been examined (without mismatch), this happens if counter j (+1) == n
            if j+1 == m:
                return True  # match
    return False  # mismatch (after outer loop finished without match)


def alternative_contains(txt, pat):
    n = len(txt)
    m = len(pat)

    i = 0
    j = 0
    while i < n and j < m:  # runs as long as there are more characters in text or pattern string
        if txt[i] == pat[j]:  # match, increase both counters
            j += 1
        else:  # no match, decrease i counter and reset j
            #print('no match')
            i -= j
            j = 0
        i += 1  # examine character by character

        # two possibilities for end of loop (hit end of pattern or end of loop)
    if j == m:  # found (hit end of pattern)
        return True
    else:  # not found (hit end of text)
        return False


if __name__ == '__main__':
    print(alternative_contains('ABDKJFLDSCDSKFJDKJFMIKAKDFJLKSFJ', 'MIKA'))
