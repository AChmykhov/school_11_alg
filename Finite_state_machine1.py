
class State:
    def __init__(self,parent = None, route = None, childrens=None, is_term=True):
        if childrens is None:
            self.childrens = {}
        else:
            self.childrens = childrens
        if parent and route:
            parent.childrens[route] = self
            parent.is_term = False
        self.is_term = is_term

    def check_word(self, word):
        if word:
            if word[0] in self.childrens:
                return self.childrens[word[0]].check_word(word[1:])
        else:
            return self.is_term





root = State()
# words_to_start = list(map(int, input().split()))
words_to_start = ["кот", "кошка", "мыло", "мыть", "мы", "мыло"]

for a in words_to_start:
    for i in range(0, len(a)):
        if i == 0:
            tmp = State(parent=root, route=a[i])
        else:
            tmp = State(tmp, a[i])




