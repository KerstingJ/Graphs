import sys


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


words = set()

with open('words.txt', 'r') as f:
    count = 0
    for line in f:
        line = line[:-1]
        words.add(line.lower())


def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)

            if w != word and w in words:
                neighbors.append(w)

    return neighbors


def find_word_ladder(begin, end):
    visited = set()
    q = Queue()
    q.enqueue([begin])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == end:
                return path

            for neighbor in get_neighbors(v):
                q.enqueue(path + [neighbor])

    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("program expects to be run as follows\npython wordtransform.py word1 word2")
    else:
        w1 = sys.argv[1]
        w2 = sys.argv[2]
        if len(w1) != len(w2):
            print("please provide 2 equal length words")
        else:
            print(w1, w2)
            print(find_word_ladder(w1, w2))
