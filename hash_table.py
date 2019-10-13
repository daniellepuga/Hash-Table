# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = [ [] for i in range(self.size)]     

    def hash(self, key):
        size = (self.size)
        return hash(key) % size
        
    def __setitem__(self, key, value):
        key_hash = self.hash(key)
        key_value = [key, value]

        if self.data[key_hash] is not None:
            for k in self.data[key_hash]:
                if k[0] == key:
                    k[1] = value
                    return True
            self.data[key_hash].append(key_value)
        else:
            self.data[key_hash].append([key, value])

    def __getitem__(self, key):
        index = self.hash(key)
        for k in self.data[index]: #looping through all keys
            if k[0] == key: #if k equals key we are looking for, the key sent into the method
                return k[1]

    # def delete(self, key, value):

    def clear(self):
        
