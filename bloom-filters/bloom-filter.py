import math
import hashlib
import random
import string
from bitarray import bitarray

class BloomFilter:
    def __init__(self, n, p=0.01):
        self.m = int(-n * math.log(p) / (math.log(2) ** 2))
        self.k = int(-math.log(p) / math.log(2))
        self.bits = bitarray(self.m)
        self.bits.setall(0)

    def _indices(self, key):
        h1 = int(hashlib.md5(key.encode()).hexdigest(), 16)
        h2 = int(hashlib.sha1(key.encode()).hexdigest(), 16)
        return [(h1 + i * h2) % self.m for i in range(self.k)]

    def insert(self, key):
        for i in self._indices(key):
            self.bits[i] = 1

    def contains(self, key):
        return all(self.bits[i] for i in self._indices(key))


def basic_test():
    print("=== Basic test ===")
    bf = BloomFilter(n=1000, p=0.01)
    for word in ["apple", "banana", "cherry"]:
        bf.insert(word)

    print(f"contains('apple')  -> {bf.contains('apple')}")
    print(f"contains('banana') -> {bf.contains('banana')}")
    print(f"contains('cherry') -> {bf.contains('cherry')}")
    print(f"contains('grape')  -> {bf.contains('grape')}")


def random_word(length=8):
    return "".join(random.choices(string.ascii_lowercase, k=length))


def false_positive_test():
    print("\n=== False positive rate test ===")
    target_p = 0.01
    n = 10000
    checks = 10000

    bf = BloomFilter(n=n, p=target_p)
    print(f"Filter size (m): {bf.m} bits ({bf.m / 8 / 1024:.1f} kB)")
    print(f"Number of hash functions (k): {bf.k}")

    inserted = set()
    while len(inserted) < n:
        inserted.add(random_word())
    for w in inserted:
        bf.insert(w)

    false_positives = 0
    tested = 0
    while tested < checks:
        w = random_word()
        if w in inserted:
            continue
        tested += 1
        if bf.contains(w):
            false_positives += 1

    measured = false_positives / tested
    print(f"Target false positive rate:   {target_p:.2%}")
    print(f"Measured false positive rate: {measured:.2%}")


if __name__ == "__main__":
    basic_test()
    false_positive_test()
