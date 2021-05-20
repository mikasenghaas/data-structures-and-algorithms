# find the perfect hash function for some input

def perfect_hash_function(arr):
    # bruteforce
    for m in range(2, 100):
        for a in range(1, 1000):
            hashes = set()
            for val in arr:
                hashes.add((a * hash(val) % m))
            if len(hashes) == len(arr):
                return (m, a)


print(perfect_hash_function(['jonas', 'mika', 'test', 'noway']))
