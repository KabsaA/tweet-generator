from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __iter__(self):
        """ Iterates through the tuples in the list """
        for node in self.items():
            yield node


    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table
        Constant runtime n being lenght O(n)"""

        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table
        Best Case - Constant runtime O(n)"""

        all_values = []
        for bucket in self.buckets:
            for key,value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table
        Constant time complexity O(n) """
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items
        print(all_items)

    def length(self):
        """Return the number of key-value entries - O(1) - constant - Best Case"""
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False
        O(1) - constant - Best Case
        O(n) - Linear - worst case"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def get(self, key):
        """Return the value for given key or return KeyError.
                O(1) - constant - Best Case"""
        index = self._bucket_index(key)
        ll = self.buckets[index]
        node_data = ll.find(lambda item: item[0] == key)
        if node_data is None:
            raise KeyError('Key not found: {}'.format(key))
        else:
            return node_data[1]


    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        index = self._bucket_index(key)
        ll = self.buckets[index]

        node_data = ll.find(lambda item: item[0] == key)
        if node_data == None:
            ll.append((key, value))
            self.size += 1

        else:
            ll.delete(node_data)
            ll.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or return KeyError
                O(1) - constant - Best Case"""
        index = self._bucket_index(key)
        ll = self.buckets[index]
        node_data = ll.find(lambda item: item[0] == key)
        if node_data == None:
            raise KeyError('Key not found: {}'.format(key))
        else:
            ll.delete(node_data)
            self.size -= 1

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self.size

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
