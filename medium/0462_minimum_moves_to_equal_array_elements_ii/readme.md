**Solution: 462. Minimum Moves to Equal Array Elements II**

### Problem Restatement
Given an integer array `nums`, in one move you can increment or decrement any element by `1`. Return the minimum total moves to make all elements equal.

### Key Observation
Making all elements equal to a target value `t` costs $\sum |nums[i] - t|$ moves — i.e. the **sum of absolute differences** between every element and `t`.

### Why the Median?
We want to minimize $f(t)=\sum_{i}|nums[i]-t|$.

This is the classic **geometric median (1-D)** problem. The function is minimized when `t` is a **median** of the dataset:
- As `t` increases past a data point, the slope of $f$ changes by `+2` (one fewer point is to the right, one more to the left).
- The minimum occurs where the number of points on the left equals the number on the right — exactly the definition of the median.

*(Contrast: minimizing $\sum (nums[i]-t)^2$ gives the **mean**, because squaring penalizes large deviations more heavily.)*

### Why Not the Mean?
Absolute distance is robust to outliers. Example `[1, 100, 100]`:
- Median `100` → cost = 99 + 0 + 0 = **99**
- Mean `67` → cost ≈ 66 + 33 + 33 = **132** (worse)

So the mean can be pulled toward outliers and is suboptimal for L1 distance.

### Algorithm (high level)
1. Sort `nums` (or find the median in $O(n)$ via selection).
2. Choose median `m = nums[⌊n/2⌋]`.
3. Answer = $\sum |nums[i] - m|$.

For even `n`, either of the two middle elements yields the same minimal sum.

### Complexity
- **Time:** $O(n \log n)$ with sorting, or $O(n)$ expected with quickselect.
- **Space:** $O(1)$ auxiliary.

### Conclusion
The minimum moves equals the total Manhattan (L1) distance from all elements to the **median**. ✅

