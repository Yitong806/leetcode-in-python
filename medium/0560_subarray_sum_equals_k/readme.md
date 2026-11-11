# 0560. Subarray Sum Equals K

## Problem

Given an array of integers `nums` and an integer `k`, return the total number of **subarrays** whose sum equals `k`.

A subarray is a contiguous non-empty sequence of elements within the array.

---

## Approach

### Brute Force (O(n²)) — for reference

Enumerate every `(left, right)` pair, compute the running sum, and count matches.

```python
def on2_brute_force(self, nums, k):
    fit = 0
    for left in range(len(nums)):
        current_sum = 0
        for right in range(left, len(nums)):
            current_sum += nums[right]
            if current_sum == k:
                fit += 1
    return fit
```

This works but times out on large inputs (n ≤ 2×10⁴).

---

### Optimized: Prefix Sum + Hash Map (O(n))

#### Key Insight

For any subarray `nums[i..j]`, its sum equals:

```
sum(i..j) = prefix_sum[j] - prefix_sum[i-1]
```

We want `sum(i..j) == k`, which means:

```
prefix_sum[j] - prefix_sum[i-1] == k
⇔  prefix_sum[i-1] == prefix_sum[j] - k
```

So at each position `j`, if we know **how many previous prefix sums equal `prefix_sum[j] - k`**, we immediately know how many valid subarrays end at `j`.

#### Algorithm

1. Maintain a hash map `prefix_sum_cnt` counting occurrences of each prefix sum seen so far. Initialize with `{0: 1}` to handle subarrays starting from index `0`.
2. Traverse `nums`, accumulating `current_prefix_sum`.
3. At each step, compute `target_rest = current_prefix_sum - k`. Add `prefix_sum_cnt[target_rest]` to the answer.
4. Increment the count for `current_prefix_sum` in the map.

#### Why `{0: 1}` Is Needed

If `current_prefix_sum == k` at some index `j`, then `target_rest = 0`. We need the map to record that a prefix sum of `0` has occurred once (before the array starts), so this case is counted correctly.

#### Example Walkthrough

`nums = [1, 2, 3], k = 3`

| i | num | prefix_sum | target_rest | map before lookup | fit added | map after update |
|---|-----|-----------|-------------|-------------------|-----------|------------------|
| — | — | 0 | — | `{0:1}` | — | — |
| 0 | 1 | 1 | 1−3=−2 | `{0:1}` | 0 | `{0:1, 1:1}` |
| 1 | 2 | 3 | 3−3=0 | `{0:1, 1:1}` | +1 | `{0:1, 1:1, 3:1}` |
| 2 | 3 | 6 | 6−3=3 | `{0:1, 1:1, 3:1}` | +1 | `{0:1, 1:1, 3:1, 6:1}` |

Result: **2** (subarrays `[1,2]` and `[3]`).

---

## Complexity

- **Time**: O(n) — single pass, each hash map operation is O(1) average.
- **Space**: O(n) — the hash map stores at most n+1 distinct prefix sums.

---

## Key Takeaway

> **Prefix sum + hash map** converts "count subarrays with sum k" from O(n²) brute force into O(n). The pattern applies broadly: whenever you need to count contiguous subarrays satisfying a sum condition, think prefix sum + complement lookup.