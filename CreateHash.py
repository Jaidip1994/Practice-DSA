class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for elem in key:
            hash += ord(elem)
        return hash % self.MAX

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for i in range(self.arr[hash]):
            if i[0] == key:
                return i[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        print(self.arr[h])
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))

    def __delitem__(self, key):
        hash = self.get_hash(key)
        for idx, elem in enumerate(self.arr[hash]):
            if elem[0] == key:
                del self.arr[hash][idx]
                break


if __name__ == "__main__":
    t = HashTable()
    print(t.get_hash("march 6"))

    t["march 6"] = 29
    t["march 6"] = 229
    t["march 7"] = 29
    t["march 17"] = 329
    print(t.arr)

    del t["march 17"]
    print(t.arr)
