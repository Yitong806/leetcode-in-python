class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        kv: dict[frozenset, list[str]] = {}
        for s in strs:
            counts = {}
            for c in s:
                counts[c] = counts.get(c, 0) + 1
            k = tuple(sorted(counts.items()))
            if k not in kv.keys():
                kv[k] = []
            kv[k].append(s)
        return list(kv.values())