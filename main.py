import hashlib

class CountingBloomFilter:
    def __init__(self, m=256, k=3): self.m, self.k, self.cnt = m, k, [0]*m
    def _pos(self, x):
        h = int(hashlib.sha256(x.encode()).hexdigest(), 16)
        return [((h >> (16*i)) & 0xFFFF) % self.m for i in range(self.k)]
    def add(self, x):
        for p in self._pos(x): self.cnt[p] += 1
    def remove(self, x):
        if x in self:
            for p in self._pos(x): self.cnt[p] = max(0, self.cnt[p] - 1)
    def __contains__(self, x): return all(self.cnt[p] > 0 for p in self._pos(x))

if __name__ == "__main__":
    cbf = CountingBloomFilter(); cbf.add("tok1"); assert "tok1" in cbf
    cbf.remove("tok1"); assert "tok1" not in cbf
    print("[PASS] 022_counting_bloom_filter")
