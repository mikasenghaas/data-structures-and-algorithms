# python implementation of the kmp substring search algorithm

# O(m+n) in the worst-case
class KMP:
    def __init__(self, txt):
        self.txt = txt
        self.n = len(txt)

    @staticmethod
    def build_dfa(pat, r=256):
        dfa = [[0 for _ in range(0, len(pat))] for _ in range(0, r)]

        dfa[ord(pat[0])][0] = 1  # set next state in first col
        X = 0
        for j in range(1, len(pat)):  # every col (length of pattern)
            # Compute dfa[][j]
            for c in range(0, r):
                dfa[c][j] = dfa[c][X]  # copy mismatch cases
            dfa[ord(pat[j])][j] = j + 1  # set match case (next stage)
            X = dfa[ord(pat[j])][X]  # update restart state
        return dfa

    def search(self, pat):
        n = len(self.txt)
        m = len(pat)

        dfa = self.build_dfa(pat)

        i = 0
        j = 0
        while i < n and j < m:
            # builds on alternative algorithm but sets back based on automaton
            j = dfa[ord(self.txt[i])][j]
            i += 1
        if j == m:  # found (hit end of pattern)
            return True
        else:  # not found (hit end of text)
            return False


if __name__ == '__main__':
    kmp = KMP('DFKJSLDFJDFFJKSDJFMIKAKJDFJSDKLJCDSNFNSDKFNDFKMDF')
    print(kmp.search('MIKA'))
