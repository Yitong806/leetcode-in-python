class Solution:
    def can_merge(self, a, b) -> bool:
        return max(a[1], b[1]) - min(a[0], b[0]) <= a[1] - a[0] + b[1] - b[0]

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda a: a[0])
        current_start, current_end = -1, -1
        merged = []
        for i in range(len(intervals)):
            if current_start == -1:
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                continue
            if self.can_merge([current_start, current_end], intervals[i]):
                current_start = min(current_start, intervals[i][0])
                current_end = max(current_end, intervals[i][1])
            else:
                merged.append([current_start, current_end])
                current_start = intervals[i][0]
                current_end = intervals[i][1]

        if current_start != -1 and current_end != -1:
            merged.append([current_start, current_end])

        return merged
